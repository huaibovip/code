
https://zenodo.org/record/583096


Gold Atlas - Male Pelvis - Gentle Radiotherapy
Nyholm, Tufve; Svensson, Stina; Andersson, Sebastian; Jonsson, Joakim; Sohlin, Maja; Gustavsson, Christian; Kjellen, Elisabeth; Albertsson, Per; Blomqvist, Lennart; Zackrisson, Björn; Olsson, Lars E.; Gunnlaugsson, Adalsteinn

Magnetic resonance images (MRI) (T1w and T2w) with flat table top, and CT images of 19 male patients. The imaging was performed over the pelvic region. In addition there is a CT image that is deformably registered to the MR data. 5 expert observers have independently delineated organs relevant for radiotherapy on all patients. Also included is a consensus delineation of each structure and a STAPLE.

All data is stored in DICOM format.

A publication describing the data set in detail is submitted.

The purpose of the dataset is training or validation of methods for automatic segmentation or conversion from MR to CT.

Please cite:

Nyholm, Tufve, Stina Svensson, Sebastian Andersson, Joakim Jonsson, Maja Sohlin, Christian Gustafsson, Elisabeth Kjellén, et al. 2018. “MR and CT Data with Multi Observer Delineations of Organs in the Pelvic Area - Part of the Gold Atlas Project.” Medical Physics 12 (10): 3218–21. doi:10.1002/mp.12748.

 

ELASTIX parameter files used:

Registration site 1. 

(FixedInternalImagePixelType "float")

(MovingInternalImagePixelType "float")
(FixedImageDimension 3)
(MovingImageDimension 3)
(UseDirectionCosines "true")

// **************** Main Components **************************
(Registration "MultiMetricMultiResolutionRegistration")
(ResampleInterpolator "FinalBSplineInterpolator")
(Resampler "OpenCLResampler")
(OpenCLResamplerUseOpenCL "true")
(FixedImagePyramid "FixedSmoothingImagePyramid"  "FixedSmoothingImagePyramid" )
(MovingImagePyramid "MovingSmoothingImagePyramid"  "MovingSmoothingImagePyramid" )
(Interpolator "BSplineInterpolator" "BSplineInterpolator" )
(Metric "NormalizedMutualInformation" "AdvancedMeanSquares")
(Metric0Weight 30000)
(Metric1Weight 1)
(Optimizer "AdaptiveStochasticGradientDescent")
(Transform "BSplineTransform")

// ******************** Multiresolution **********************
(NumberOfResolutions 3)
(ImagePyramidSchedule 4.0 4.0 4.0 2.0 2.0 2.0 1.0 1.0 1.0)

// ***************** Transformation **************************
(FinalGridSpacingInPhysicalUnits 60 60 60)
(GridSpacingSchedule 4 2 1)
(AutomaticScalesEstimation "true")
(AutomaticTransformInitialization "false")
(HowToCombineTransforms "Compose")

// ******************* Optimizer ****************************
(MaximumNumberOfIterations 500 500 500)

// ******************* Similarity measure *********************
(NumberOfHistogramBins 64 96 96)
(ErodeMask "false")

// **************** Image sampling **********************
(NumberOfSpatialSamples 3000)
(NewSamplesEveryIteration "true")
(ImageSampler "RandomCoordinate" "RandomCoordinate")
(CheckNumberOfSamples "true")
(RequiredRatioOfValidSamples 0.01)
(UseRandomSampleRegion "true")
(SampleRegionSize 150 150 70) 
(MaximumNumberOfSamplingAttempts 100) 

// ************* Interpolation and Resampling ****************
(BSplineInterpolationOrder 2)
(FinalBSplineInterpolationOrder 3)
(DefaultPixelValue -1)
(WriteResultImage "false")
(ResultImagePixelType "short")
(ResultImageFormat "mhd")

 

Registration site 2:

(FixedInternalImagePixelType "float")
(MovingInternalImagePixelType "float")
(FixedImageDimension 3)
(MovingImageDimension 3)
(UseDirectionCosines "true")

// **************** Main Components **************************
(Registration "MultiMetricMultiResolutionRegistration")
(ResampleInterpolator "FinalBSplineInterpolator")
(Resampler "OpenCLResampler")
(OpenCLResamplerUseOpenCL "true")
(FixedImagePyramid "FixedSmoothingImagePyramid"  "FixedSmoothingImagePyramid" )
(MovingImagePyramid "MovingSmoothingImagePyramid"  "MovingSmoothingImagePyramid" )
(Interpolator "BSplineInterpolator" "BSplineInterpolator" )
(Metric "NormalizedMutualInformation" "AdvancedMeanSquares")
(Metric0Weight 15000)
(Metric1Weight 1)
(Optimizer "AdaptiveStochasticGradientDescent")
(Transform "BSplineTransform")

// ******************** Multiresolution **********************
(NumberOfResolutions 3)
(ImagePyramidSchedule 4.0 4.0 4.0 2.0 2.0 2.0 1.0 1.0 1.0)

// ***************** Transformation **************************
(FinalGridSpacingInPhysicalUnits 60 60 60)
(GridSpacingSchedule 4 2 1)
(AutomaticScalesEstimation "true")
(AutomaticTransformInitialization "false")
(HowToCombineTransforms "Compose")

// ******************* Optimizer ****************************
(MaximumNumberOfIterations 500 500 500)

// ******************* Similarity measure *********************
(NumberOfHistogramBins 64 96 96)
(ErodeMask "false")

// **************** Image sampling **********************
(NumberOfSpatialSamples 3000)
(NewSamplesEveryIteration "true")
(ImageSampler "RandomCoordinate" "RandomCoordinate")
(CheckNumberOfSamples "true")
(RequiredRatioOfValidSamples 0.01)
(UseRandomSampleRegion "false")

// ************* Interpolation and Resampling ****************
(BSplineInterpolationOrder 2)
(FinalBSplineInterpolationOrder 3)
(DefaultPixelValue -1)
(WriteResultImage "false")
(ResultImagePixelType "short")
(ResultImageFormat "mhd")

 

Registation site 3:

(FixedInternalImagePixelType "float")
(MovingInternalImagePixelType "float")
(FixedImageDimension 3)
(MovingImageDimension 3)
(UseDirectionCosines "true")

// **************** Main Components **************************
(Registration "MultiMetricMultiResolutionRegistration")
(ResampleInterpolator "FinalBSplineInterpolator")
(Resampler "OpenCLResampler")
(OpenCLResamplerUseOpenCL "true")
(FixedImagePyramid "FixedSmoothingImagePyramid"  "FixedSmoothingImagePyramid" )
(MovingImagePyramid "MovingSmoothingImagePyramid"  "MovingSmoothingImagePyramid" )
(Interpolator "BSplineInterpolator" "BSplineInterpolator" )
(Metric "NormalizedMutualInformation" "AdvancedMeanSquares")
(Metric0Weight 50000)
(Metric1Weight 1)
(Optimizer "AdaptiveStochasticGradientDescent")
(Transform "BSplineTransform")

// ******************** Multiresolution **********************
(NumberOfResolutions 3)
(ImagePyramidSchedule 4.0 4.0 4.0 2.0 2.0 2.0 1.0 1.0 1.0)

// ***************** Transformation **************************
(FinalGridSpacingInPhysicalUnits 60 60 60)
(GridSpacingSchedule 4 2 1)
(AutomaticScalesEstimation "true")
(AutomaticTransformInitialization "false")
(HowToCombineTransforms "Compose")

// ******************* Optimizer ****************************
(MaximumNumberOfIterations 50 50 100)

// ******************* Similarity measure *********************
(NumberOfHistogramBins 64 96 96)
(ErodeMask "false")

// **************** Image sampling **********************
(NumberOfSpatialSamples 3000)
(NewSamplesEveryIteration "true")
(ImageSampler "RandomCoordinate" "RandomCoordinate")
(CheckNumberOfSamples "true")
(RequiredRatioOfValidSamples 0.01)
(UseRandomSampleRegion "true")
(SampleRegionSize 150 150 70) 
(MaximumNumberOfSamplingAttempts 100) 

// ************* Interpolation and Resampling ****************
(BSplineInterpolationOrder 2)
(FinalBSplineInterpolationOrder 3)
(DefaultPixelValue -1)
(WriteResultImage "false")
(ResultImagePixelType "short")
(ResultImageFormat "mhd")