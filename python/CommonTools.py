"""
Created by Noah Jing Li (noah.jing.li@outlook.com) on May 26th, 2018
"""
import itk
import argparse
import sys


def usage():
	print("[ convert data type to .nii.gz ]")
	print("example: python CommonTools.py --convert --input inputImage --output outputImage\n")	

	print("[ display the image information ]")
	print("example: python CommonTools.py --information --input inputImage\n")	

def convert(input, output):
	image = itk.imread(input)
	InputType = type(image)
	input_dimension = image.GetImageDimension()
	OutputType = itk.Image[itk.UC, input_dimension]
	castFilter = itk.CastImageFilter[InputType, OutputType].New()
	castFilter.SetInput(image)
	itk.imwrite(castFilter, output)
	print("\nConvert\t\tDONE!\n")


parser=argparse.ArgumentParser()
parser.add_argument('--usage', action='store_true', help='display usage')
parser.add_argument('--convert', action='store_true', help='convert data type to .nii.gz')

# parameters
parser.add_argument('--input', type=str, help='input file')
parser.add_argument('--output', type=str, help='output file')


if len(sys.argv)==1:
	parser.print_help(sys.stderr)
	sys.exit(1)

args=parser.parse_args()

if args.usage == True:
	usage()
elif args.convert == True:
	print("input = {}".format(args.input))
	print("output = {}".format(args.output))
	convert(args.input, args.output)




# # import itk
# import sys
# import argparse

# def print_help():
# 	print("[ display the image information ]")
# 	print("example: ImageTools --information --in inputImage\n]")	


# # def main():

# parser = argparse.ArgumentParser(description='CommonTools for medical image processing')
# parser.add_argument('--help')
# parser.add_argument('--phase', type=str, default="test",
#                     help='configure file')

# args = parser.parse_args()

# if args.help == True:
# 	print_help()

# # ini_file = args.help
# # print(ini_file)



# # if __name__ == '__main__': 
# #     main()
