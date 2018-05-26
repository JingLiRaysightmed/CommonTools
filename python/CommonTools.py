"""
Created by Noah Jing Li (noah.jing.li@outlook.com) on May 26th, 2018
"""
#!~/.conda/envs/tf/bin python2.7
import itk
import argparse
import sys
import numpy as np

def Usage():
	print("[ convert data type to .nii.gz ]")
	print("example: python CommonTools.py --convert --input inputImage --output outputImage\n")	

	print("[ display the image information ]")
	print("example: python CommonTools.py --information --input inputImage\n")	

def Convert(input, output):
	image = itk.imread(input)
	InputType = type(image)
	input_dimension = image.GetImageDimension()
	OutputType = itk.Image[itk.UC, input_dimension]
	castFilter = itk.CastImageFilter[InputType, OutputType].New()
	castFilter.SetInput(image)
	itk.imwrite(castFilter, output)
	print("\nConvert\t\tDONE!\n")

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



#####################################################################
parser=argparse.ArgumentParser()

# mode
parser.add_argument('--usage', action='store_true', help='display usage')
parser.add_argument('--convert', action='store_true', help='convert data type to .nii.gz')
parser.add_argument('--information', action='store_true', help='display image information')

# parameters
parser.add_argument('--input', type=str, help='input file')
parser.add_argument('--output', type=str, help='output file')


if len(sys.argv)==1:
	parser.print_help(sys.stderr)
	sys.exit(1)

args=parser.parse_args()

if args.usage == True:
	Usage()

elif args.convert == True:
	print("input = {}".format(args.input))
	print("output = {}".format(args.output))
	Convert(args.input, args.output)

elif args.information == True:
	print("input = {}".format(args.input))
	Information(args.input)