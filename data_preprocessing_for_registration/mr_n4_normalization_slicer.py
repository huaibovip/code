import os
import glob
import slicer


def getParams(cliModule):
    """
    Get list of parameter names.
    """
    # cliModule = slicer.modules.grayscalemodelmaker
    n = cliModule.cliModuleLogic().CreateNode()
    for groupIndex in range(n.GetNumberOfParameterGroups()):
        print(f"Group: {n.GetParameterGroupLabel(groupIndex)}")
        for parameterIndex in range(n.GetNumberOfParametersInGroup(groupIndex)):
            print(
                "  {0} [{1}]: {2}".format(
                    n.GetParameterName(groupIndex, parameterIndex),
                    n.GetParameterTag(groupIndex, parameterIndex),
                    n.GetParameterLabel(groupIndex, parameterIndex),
                )
            )


def n4itkbiasfieldcorrection(input_path, mask_path, save_bias_filed=False):
    """
    Group: IO
    inputImageName [image]: Input Image
    maskImageName [image]: Mask Image
    outputImageName [image]: Output Volume
    outputBiasFieldName [image]: Output bias field image

    Group: N4 Parameters
    initialMeshResolution [float-vector]: BSpline grid resolution
    splineDistance [float]: Spline distance
    bfFWHM [float]: Bias field Full Width at Half Maximum

    Group: Advanced N4 Parameters
    numberOfIterations [integer-vector]: Number of iterations
    convergenceThreshold [float]: Convergence threshold
    bsplineOrder [integer]: BSpline order
    shrinkFactor [integer]: Shrink factor
    weightImageName [image]: Weight Image
    wienerFilterNoise [float]: Wiener filter noise
    nHistogramBins [integer]: Number of histogram bins
    """
    inputImageNode = slicer.util.loadVolume(input_path)
    outputImageNode = slicer.mrmlScene.AddNewNodeByClass(
        "vtkMRMLScalarVolumeNode", "n4_output"
    )

    if mask_path is not None:
        maskImageNode = slicer.util.loadLabelVolume(mask_path)
    else:
        # maskImageNode = slicer.mrmlScene.AddNewNodeByClass(
        #     "vtkMRMLLabelMapVolumeNode", "auto_mask"
        # )
        maskImageNode = None
    if save_bias_filed:
        outputBiasFieldNode = slicer.mrmlScene.AddNewNodeByClass(
            "vtkMRMLScalarVolumeNode", "bias_filed"
        )
    else:
        outputBiasFieldNode = None

    # Group: IO
    param = {}
    param["inputImageName"] = inputImageNode.GetID()
    param["outputImageName"] = outputImageNode.GetID()
    if maskImageNode is not None:
        param["maskImageName"] = maskImageNode.GetID()
    if outputBiasFieldNode is not None:
        param["outputBiasFieldName"] = outputBiasFieldNode.GetID()
    # # Group: N4 Parameters
    # param["initialMeshResolution"] = [1,1,1]
    # param["splineDistance"] = 0.0
    # param["bfFWHM"] = 0.0
    # # Group: Advanced N4 Parameters
    # param["numberOfIterations"] = [50,40,30]
    # param["convergenceThreshold"] = 0.0001
    # param["bsplineOrder"] = 3
    # param["shrinkFactor"] = 4
    # param["weightImageName"] = None
    # param["wienerFilterNoise"] = 0.0
    # param["nHistogramBins"] = 0
    # run
    cliNode = slicer.cli.runSync(
        slicer.modules.n4itkbiasfieldcorrection, parameters=param
    )
    # Process results
    if cliNode.GetStatus() & cliNode.ErrorsMask:
        # error
        errorText = cliNode.GetErrorText()
        slicer.mrmlScene.RemoveNode(cliNode)
        slicer.mrmlScene.RemoveNode(inputImageNode)
        slicer.mrmlScene.RemoveNode(outputImageNode)
        if maskImageNode is not None:
            slicer.mrmlScene.RemoveNode(maskImageNode)
        if outputBiasFieldNode is not None:
            slicer.mrmlScene.RemoveNode(outputBiasFieldNode)
        raise ValueError("CLI execution failed: " + errorText)
    # success
    slicer.mrmlScene.RemoveNode(cliNode)
    slicer.mrmlScene.RemoveNode(inputImageNode)
    if maskImageNode is not None:
        slicer.mrmlScene.RemoveNode(maskImageNode)
    if outputBiasFieldNode is not None:
        slicer.mrmlScene.RemoveNode(outputBiasFieldNode)
    return outputImageNode


if __name__ == "__main__":
    dataset_root = "/home/hb/gpu2/datasets/i2i/IXI/outputs"
    data_root = os.path.join(dataset_root, "crop_outputs")
    save_root = os.path.join(dataset_root, "n4_outputs")
    modalities = ["T1", "T2", "PD"]
    for m in modalities:
        save_dir = os.path.join(save_root, "IXI-" + m)
        os.makedirs(save_dir, exist_ok=True)
        for input_path in glob.glob(os.path.join(data_root, "IXI-" + m, "*")):
            mask_path = os.path.join(
                data_root,
                "maskes",
                "IXI-" + m,
                os.path.basename(input_path)[:-7] + "_mask.nii.gz"
            )
            try:
                output_node = n4itkbiasfieldcorrection(
                    input_path,
                    mask_path,
                )
                output_path = os.path.join(save_dir, os.path.basename(input_path))
                slicer.util.saveNode(output_node, output_path)
            except ValueError as e:
                print('n4_error:', input_path)

# /public/home/hb/softwares/slicer/Slicer --no-main-window --python-script "/public/home/hb/softwares/tool/data_preprocessing/mr_n4_normalization_slicer.py"
# nohup /opt/slicer/Slicer --no-main-window --python-script ./mr_n4_normalization_slicer.py > logs/mr_n4_normalization_slicer.log 2>&1 &
