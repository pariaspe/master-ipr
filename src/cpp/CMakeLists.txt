cmake_minimum_required(VERSION 2.8.0)

# Start a project.
project(robotClient)

find_package(YARP REQUIRED COMPONENTS os dev sig)
find_package(ASROB_YARP_DEVICES REQUIRED)

# Set up our main executables.

add_executable(robotClient robotClient.cpp)

target_link_libraries(robotClient YARP::YARP_OS
                                  YARP::YARP_init
                                  YARP::YARP_dev)


add_executable(depthClient depthClient.cpp)

target_link_libraries(depthClient YARP::YARP_OS
                                  YARP::YARP_init
                                  YARP::YARP_dev)

include(GNUInstallDirs)

install(TARGETS robotClient depthClient
        DESTINATION ${CMAKE_INSTALL_BINDIR})
