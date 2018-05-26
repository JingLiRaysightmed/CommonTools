##################################################################
# Common tools using in IPMI
project(IPMI)
   
cmake_minimum_required(VERSION 2.6)
  
  
##################################################################
# Add c++0x support
if (UNIX)
	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++0x")
endif (UNIX)

if (APPLE)
	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++0x")
endif (APPLE)

# search for depedency
###################################################################
# Find ITK.
find_package(ITK)
if(ITK_FOUND)
    include(${ITK_USE_FILE})
else(ITK_FOUND)
    message(FATAL_ERROR "ITK not found.  Please set ITK_DIR.")
endif(ITK_FOUND)

###################################################################
# Find VTK.
find_package(VTK)
if(VTK_FOUND)
    include(${VTK_USE_FILE})
else(VTK_FOUND)
    message(FATAL_ERROR "VTK not found. Please set VTK_DIR.")
endif(VTK_FOUND)

###################################################################
# Find Boost
set(Boost_USE_STATIC_LIBS ON)
set(Boost_USE_MULTITHREADED ON) 
set(Boost_USE_STATIC_RUNTIME OFF)

add_definitions( -DBOOST_ALL_NO_LIB )

find_package(Boost REQUIRED COMPONENTS system filesystem timer program_options chrono regex)
include_directories(${Boost_INCLUDE_DIRS})


###################################################################
# openmp support
if (WIN32) # windows
   set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} /openmp")
   set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /openmp") 
   add_definitions( -D_CRT_SECURE_NO_WARNINGS )
   add_definitions( -D_SCL_SECURE_NO_WARNINGS )
endif (WIN32)

if (UNIX) # UNIX 
   set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fopenmp")
   set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fopenmp")
endif(UNIX)

if (APPLE) # Apple
    message(FATAL_ERROR "mac os is currently not supported, please use windows and linux")
endif(APPLE)


# include FISH headers
include_directories(.)
include_directories(${CMAKE_SOURCE_DIR}/extern)


###################################################################
# customized configuration - Setup precompiled headers for MSVS

get_filename_component(PRECOMPILED_CPP_PATH "stdafx.cpp" ABSOLUTE)

function(setup_ipmi_app appName)

if (MSVC) # visual studio precompiled headers
   set_target_properties(${appName} PROPERTIES COMPILE_FLAGS "/Yustdafx.h")
   set_source_files_properties(${PRECOMPILED_CPP_PATH} PROPERTIES COMPILE_FLAGS "/Ycstdafx.h")
endif(MSVC)

endfunction(setup_ipmi_app)


##################################################################
# set output directory
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)


##################################################################
# set openblas libraries
if (WIN32)
  if (CMAKE_SIZEOF_VOID_P EQUAL 8)
    set(OPENBLAS_LIBRARIES ${CMAKE_SOURCE_DIR}/libs/win64/libopenblas.lib)
  else ()
    set(OPENBLAS_LIBRARIES ${CMAKE_SOURCE_DIR}/libs/win32/libopenblas.lib)
  endif ()
endif(WIN32)

if (UNIX)
  set(OPENBLAS_LIBRARIES ${CMAKE_SOURCE_DIR}/libs/linux64/libopenblas.a)
endif(UNIX)


###################################################################
# recursively add each projects
add_subdirectory(app)
