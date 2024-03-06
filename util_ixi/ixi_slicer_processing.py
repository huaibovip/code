import os
import glob


def foreground(path, dstRoot, maskRoot, ext='.nii.gz'):
    # data
    inputImage = slicer.util.loadVolume(path)
    # inputImage = getNode(inputName)
    outputImage = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode', inputImage.GetName()+'_output')
    labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode", inputImage.GetName()+'_mask')
    # params
    param = {}
    param["inputVolume"] = inputImage.GetID()
    param["outputVolume"] = outputImage.GetID()
    param["outputROIMaskVolume"] = labelmapVolumeNode.GetID()
    param["maskOutput"] = True
    param["cropOutput"] = False
    # run
    slicer.cli.runSync(slicer.modules.brainsroiauto, parameters=param)
    # save nodes
    # slicer.util.saveNode(inputImage, os.path.join(dstRoot, inputImage.GetName() + ext))
    slicer.util.saveNode(outputImage, os.path.join(dstRoot, outputImage.GetName() + ext))
    slicer.util.saveNode(labelmapVolumeNode, os.path.join(maskRoot, labelmapVolumeNode.GetName() + ext))
    # remove nodes
    slicer.mrmlScene.RemoveNode(inputImage)
    slicer.mrmlScene.RemoveNode(outputImage)
    slicer.mrmlScene.RemoveNode(labelmapVolumeNode)


ROOT = r'G:\datasets\IXI\raw\IXI-PD'
subdirs = ['Guys', 'HH', 'IOP']

for subdir in subdirs:
    modal = ROOT[-2:]
    paths = glob.glob(os.path.join(ROOT, subdir, '*'))
    print(len(paths))
    DST_ROOT = os.path.join(ROOT, 'precessing', 'foreground', modal, subdir)
    MASK_ROOT = os.path.join(ROOT, 'precessing', 'mask', modal, subdir)
    os.makedirs(DST_ROOT, exist_ok=True)
    os.makedirs(MASK_ROOT, exist_ok=True)
    for path in paths:
        foreground(path, DST_ROOT, MASK_ROOT)
