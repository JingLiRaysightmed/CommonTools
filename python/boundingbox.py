import itk
import sys

input_filename = '/home/ruixin/Desktop/trans_ct_train_1001_label.nii.gz'
output_filename = '/home/ruixin/Desktop/output_trans_ct_train_1001_label.nii.gz'

# median = itk.MedianImageFilter.New(image, Radius=2)
# itk.imwrite(median, output_filename)

# //1. read the binary image
# typedef itk::ImageMaskSpatialObject<3>      ImageMaskSpatialObject;
# typedef ImageMaskSpatialObject::ImageType   ImageType;
# typedef ImageType::RegionType               RegionType;
# typedef itk::ImageFileReader< ImageType >   ReaderType;
# ReaderType::Pointer reader = ReaderType::New();
# reader->SetFileName(input_path.c_str());
# try
# {
# 	reader->Update();
# }
# catch (itk::ExceptionObject & excp)
# {
# 	std::cerr << excp << std::endl;
# 	return EXIT_FAILURE;
# }
image = itk.imread(input_filename)
# InputType = itk.Image[itk.]
maskSO = itk.ImageMaskSpatialObject()
maskSO.SetImage(image)
boundingBoxRegion = maskSO.GetAxisAlignedBoundingBoxRegion()
print(boundingBoxRegion)

# # //2. get the bounding box
# ImageType::Pointer image = reader->GetOutput();

# ImageMaskSpatialObject::Pointer maskSO = ImageMaskSpatialObject::New();
# maskSO->SetImage(image);
# RegionType boundingBoxRegion = maskSO->GetAxisAlignedBoundingBoxRegion();
# std::cout << "Bounding Box Region: " << boundingBoxRegion << std::endl;

# ImageType::IndexType box_start = boundingBoxRegion.GetIndex();
# ImageType::SizeType box_size = boundingBoxRegion.GetSize();

# std::cout << "Box start index = " << box_start[0] << " " << box_start[1] << " " << box_start[2] << "\n";
# std::cout << "Box size = " << box_size[0] << " " << box_size[1] << " " << box_size[2] << "\n";

# ImageType::IndexType box_end;
# box_end[0] = box_start[0] + box_size[0] - 1;
# box_end[1] = box_start[1] + box_size[1] - 1;
# box_end[2] = box_start[2] + box_size[2] - 1;

# std::cout << "Box end index = " << box_end[0] << " " << box_end[1] << " " << box_end[2] << "\n";

# //3. transform the start point and end point from voxel coordinate to world coordinate
# typedef itk::Point<double, ImageType::ImageDimension> PointType;
# PointType world_start, world_end;

# image->TransformIndexToPhysicalPoint(box_start, world_start);
# image->TransformIndexToPhysicalPoint(box_end, world_end);

# std::cout << "start point's world coordinate = " << world_start[0] << ", " << world_start[1] << ", " << world_start[2] << std::endl;
# std::cout << "end point's world coordinate = " << world_end[0] << ", " << world_end[1] << ", " << world_end[2] << std::endl;

# //4. output the two points world coordinate to txt file
# //start point 
# std::ofstream start_file(start_pt, std::ios::out);
# if (!start_file)
# {
# 	std::cout << "Error opening file for writing." << std::endl;
# 	return EXIT_FAILURE;
# }

# start_file << world_start[0] << " " << world_start[1] << " " << world_start[2] << "\n";

# start_file.close();

# //end point
# std::ofstream end_file(end_pt, std::ios::out);
# if (!end_file)
# {
# 	std::cout << "Error opening file for writing." << std::endl;
# 	return EXIT_FAILURE;
# }

# end_file << world_end[0] << " " << world_end[1] << " " << world_end[2] << "\n";

# end_file.close();
