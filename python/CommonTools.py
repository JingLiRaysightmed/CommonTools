"""
Created by Noah Jing Li (noah.jing.li@outlook.com) on May 26th, 2018
"""
#!~/.conda/envs/tf/bin python2.7
from __future__ import division
import itk
import argparse
import sys
import numpy as np
# import SimpleITK as sitk

def Usage():
	print("[ convert data type to .nii.gz ]")
	print("example: python CommonTools.py --convert --input inputImage --output outputImage\n")	

	print("[ display the image information ]")
	print("example: python CommonTools.py --information --input inputImage\n")

	print("[ resample image ]")
	print("example: python CommonTools.py --resample_self --input inputImage --output outputImage --spacing tuple\n")

	print("[ generate the segmentation ]")
	print("example: python CommonTools.py --generate_segment --in probabilityMap --threshold value --out segmentationImage\n")

	print("[ get bounding box ]")
	print("example: ImageTools --boundingbox --in inputImage --start_pt filename --end_pt filename\n")

def Convert(input, output):
	image = itk.imread(input)
	InputType = type(image)
	input_dimension = image.GetImageDimension()
	OutputType = itk.Image[itk.UC, input_dimension]
	castFilter = itk.CastImageFilter[InputType, OutputType].New()
	castFilter.SetInput(image)
	itk.imwrite(castFilter, output)
	print("Convert\tDONE!")

def Information(input):
	image = itk.imread(input)
	print(image)

	PixelType = type(image)
	Dimension = image.GetImageDimension()
	origin = image.GetOrigin()
	spacing = image.GetSpacing()
	direction = image.GetDirection()
	size = image.GetLargestPossibleRegion().GetSize()

	print("PixelType = {}".format(PixelType))
	print("Dimension = {}".format(Dimension))
	print("origin = {}".format(origin))
	print("spacing = {}".format(spacing))
	print("direction = {}".format(direction))
	print("size = {}".format(size))
	print("Information\tDONE!")

def ResampleSelf(input, output, spacing):
	"""
	Step: 1. load the image 
		  2. compute the resample size
		  3. output the image to file
	"""
	# 1. load the image
	image = itk.imread(input)
	ImageType = type(image)
	Dimension = image.GetImageDimension()
	size = image.GetLargestPossibleRegion().GetSize()
	old_spacing = image.GetSpacing()

	# 2. compute the resample size
	spacing = np.array([spacing, spacing, spacing])
	# print("spacing = {}".format(spacing))

	phy_size = np.zeros(3, dtype=np.float64)
	resampleSize = np.zeros(3, dtype=np.float64)

	size = np.asarray(size)
	old_spacing = np.asarray(old_spacing)

	for i in np.arange(Dimension):
		phy_size[i] = size[i] * old_spacing[i]
		resampleSize[i] = phy_size[i] / spacing[i] + 0.5

	resampleSize = resampleSize.astype(int)
	print("resampleSize = {}".format(resampleSize))

	TransformType = itk.IdentityTransform[itk.D, Dimension]
	transform = TransformType.New()
	transform.SetIdentity()

	InterpolatorType = itk.NearestNeighborInterpolateImageFunction[ImageType, itk.D]
	interpolator = InterpolatorType.New()

	ResampleFilterType = itk.ResampleImageFilter[ImageType, ImageType]
	resampleFilter = ResampleFilterType.New()

	resampleFilter.SetTransform(transform)
	resampleFilter.SetInterpolator(interpolator)
	resampleFilter.SetOutputOrigin(image.GetOrigin())
	resampleFilter.SetOutputSpacing(spacing)
	resampleFilter.SetSize(resampleSize)
	resampleFilter.SetOutputDirection(image.GetDirection())
	resampleFilter.SetDefaultPixelValue(0)
	resampleFilter.SetInput(image)

	itk.imwrite(resampleFilter.GetOutput(), output)
	print("ResampleSelf\tDONE!")

def GenegrateSegment(input, threshold, output):
	"""
	//Goal: generate the segmentation based on different label's probability map
	//Step: 1. load foreground probability map
	//		2. compare the value of probability map with threshold and set the label to label map
	//		3. output the label map to file
	"""
	# 1. load two probability map
	PixelType = itk.ctype("float")
	image = itk.imread(input, PixelType)
	ImageType = type(image)
	Dimension = image.GetImageDimension()
	size = image.GetLargestPossibleRegion().GetSize()
	print("size = {}".format(size))

	# 2. compare the value of probability map with threshold and set the label to label map
	np_img = itk.GetArrayFromImage(image)
	print("np_img.shape = {}".format(np_img.shape))

	seg_img = np.zeros(np_img.shape, dtype=np.uint8)
	seg_img[np_img >= threshold] = 1
	print(np.unique(seg_img))

	# 3. output the label map to file
	itk_seg_img = itk.GetImageFromArray(seg_img)
	print("itk_seg_img.shape = {}".format(itk_seg_img.GetLargestPossibleRegion().GetSize()))
	print(type(image))
	itk.imwrite(itk_seg_img, output)

	print("GenegrateSegment\tDONE!")

#####################################################################
parser=argparse.ArgumentParser()

# mode
parser.add_argument('--usage', action='store_true', help='display usage')
parser.add_argument('--convert', action='store_true', help='convert data type to .nii.gz')
parser.add_argument('--information', action='store_true', help='display image information')
parser.add_argument('--resample_self', action='store_true', help='resample image')
parser.add_argument('--generate_segment', action='store_true', help='resample image')
parser.add_argument('--boundingbox', action='store_true', help='resample image')


# parameters
parser.add_argument('--input', type=str, help='input file')
parser.add_argument('--output', type=str, help='output file')
parser.add_argument('--spacing', type=float, default=1, help='spacing')
parser.add_argument('--threshold', type=float, default=0.75, help='threshold')
parser.add_argument('--start_pt', type=str, help='start_pt')
parser.add_argument('--end_pt', type=str, help='end_pt')

if len(sys.argv) == 1:
	parser.print_help(sys.stderr)
	sys.exit(1)

args = parser.parse_args()

if args.usage == True:
	Usage()

elif args.convert == True:
	print("input = {}".format(args.input))
	print("output = {}".format(args.output))
	Convert(args.input, args.output)

elif args.information == True:
	print("input = {}".format(args.input))
	Information(args.input)

elif args.resample_self == True:
	print("input = {}".format(args.input))
	print("output = {}".format(args.output))
	print("spacing = {}".format(args.spacing))
	ResampleSelf(args.input, args.output, args.spacing)

elif args.generate_segment == True:
	print("input = {}".format(args.input))
	print("output = {}".format(args.output))
	print("threshold = {}".format(args.threshold))
	GenegrateSegment(args.input, args.threshold, args.output)
