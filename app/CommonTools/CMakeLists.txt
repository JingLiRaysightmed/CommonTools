# Common tools for manipulating the image and mesh

option( BUILD_CommonTools "Build Common Tools" ON )

if( BUILD_CommonTools )

	#############################################
	# image tools
	add_executable(ImageTools ImageTools.cpp ../../stdafx.cpp)
	target_link_libraries(ImageTools ${ITK_LIBRARIES} ${VTK_LIBRARIES} ${Boost_LIBRARIES})
	setup_ipmi_app(ImageTools)

endif()