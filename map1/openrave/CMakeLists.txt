# Copyright: 2014 UC3M
# Author: Juan G Victores
# CopyPolicy: Released under the terms of the GNU GPL v2.0.

set(appname openrave)

find_package(YARP REQUIRED)

# Load YARP modules.
if(YARP_VERSION_SHORT VERSION_LESS 2.3.70)
    list(APPEND CMAKE_MODULE_PATH ${YARP_MODULE_PATH})
    include(YarpInstallationHelpers)
endif()

yarp_configure_external_installation(master-ipr)

#yarp_install(FILES ymanager.ini DESTINATION ${2018_PTMR_DATA_INSTALL_DIR})  # Cleaner than ${2018_PTMR_ROBOTS_INSTALL_DIR}/../ or similar.

file(GLOB xml ${CMAKE_CURRENT_SOURCE_DIR}/*.xml)
file(GLOB ecro ${CMAKE_CURRENT_SOURCE_DIR}/ecro/*.xml)
file(GLOB ecro/models ${CMAKE_CURRENT_SOURCE_DIR}/ecro/models/*.wrl)

yarp_install(FILES ${xml} DESTINATION ${2018-PTMR_CONTEXTS_INSTALL_DIR}/${appname})
yarp_install(FILES ${ecro} DESTINATION ${2018-PTMR_CONTEXTS_INSTALL_DIR}/${appname}/ecro)
yarp_install(FILES ${ecro/models} DESTINATION ${2018-PTMR_CONTEXTS_INSTALL_DIR}/${appname}/ecro/models)
yarp_install(PROGRAMS iprSim1 DESTINATION ${CMAKE_INSTALL_BINDIR})
