
#ifndef __stdafx_h__
#define __stdafx_h__

#define _USE_MATH_DEFINES
#include <math.h>

// boost headers
#include <boost/filesystem/operations.hpp>
#include <boost/filesystem/path.hpp>
#include <boost/program_options.hpp>
#include <boost/numeric/ublas/io.hpp>
#include <boost/numeric/ublas/lu.hpp>
#include <boost/numeric/ublas/matrix.hpp>
#include <boost/random/uniform_real_distribution.hpp>
#include <boost/random/uniform_int_distribution.hpp>
#include <boost/random/mersenne_twister.hpp>
#include <boost/random/normal_distribution.hpp>
#include <boost/lexical_cast.hpp>
#include <boost/property_tree/ptree.hpp>
#include <boost/property_tree/ini_parser.hpp>
#include <boost/timer/timer.hpp>
#include <boost/array.hpp>
#include <boost/graph/graph_traits.hpp>
#include <boost/graph/adjacency_list.hpp>
#include <boost/graph/dijkstra_shortest_paths.hpp>
#include <boost/property_map/property_map.hpp>
#include <boost/regex.hpp>

//Noah add


// ITK headers
#include "itkAdaptiveHistogramEqualizationImageFilter.h"
#include "itkAffineTransform.h"
//#include "itkAnalyzeImageIO.h"
#include "itkBinaryBallStructuringElement.h"
#include "itkBinaryDilateImageFilter.h"
#include "itkBinaryErodeImageFilter.h"
#include "itkCastImageFilter.h"
#include "itkChangeInformationImageFilter.h"
#include "itkConnectedComponentImageFilter.h"
#include "itkExtractImageFilter.h"
#include "itkHistogramMatchingImageFilter.h"
#include "itkImage.h"
#include "itkImageFileReader.h"
#include "itkImageFileWriter.h"
#include "itkImageMaskSpatialObject.h"
#include "itkImageRegionIterator.h"
#include "itkIdentityTransform.h"
#include "itkImageRegionIterator.h"
#include "itkBSplineInterpolateImageFunction.h"
#include "itkLinearInterpolateImageFunction.h"
#include "itkLabelImageGaussianInterpolateImageFunction.h"
#include "itkLabelShapeKeepNObjectsImageFilter.h"
#include "itkNearestNeighborInterpolateImageFunction.h"
#include "itkNormalizeImageFilter.h"
#include <itkOffset.h>
#include "itkOrientImageFilter.h"
#include "itkResampleImageFilter.h"
#include "itkRescaleIntensityImageFilter.h"
#include "itkScaleTransform.h"
#include "itkStatisticsImageFilter.h"
#include "itksys/SystemTools.hxx"
#include "itkVotingBinaryHoleFillingImageFilter.h"
//End Noah add


#endif

