#-----------------------------------------------------------------------------
cmake_minimum_required(VERSION 3.13.0)
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Module name
#   - Usually identique to the directory name)
#   - You shouldn't call 'project(...)'. See CjyxConfig.cmake for more details.
#-----------------------------------------------------------------------------
set(EXTENSION_NAME MultiVolumeImporter)

#-----------------------------------------------------------------------------
# Prerequisites
#-----------------------------------------------------------------------------
if(NOT Cjyx_SOURCE_DIR)
  set(EXTENSION_HOMEPAGE "http://www.cjyx.org/cjyxWiki/index.php/Cjyx4:Developers:Projects:QtCjyx/Tutorials/ExtensionWriting")
  set(EXTENSION_CATEGORY "Examples")
  set(EXTENSION_STATUS "Beta")
  set(EXTENSION_DESCRIPTION "This is an example of scripted Qt loadable module built as an extension")
  set(EXTENSION_DEPENDS NA) # Specified as a space separated list or 'NA' if any

  find_package(Cjyx REQUIRED)

  # Additional C/CXX flags - Should be defined before including Cjyx_USE_FILE
  set(ADDITIONAL_C_FLAGS "" CACHE STRING "Additional ${EXTENSION_NAME} C Flags")
  set(ADDITIONAL_CXX_FLAGS "" CACHE STRING "Additional ${EXTENSION_NAME} CXX Flags")

  include(${Cjyx_USE_FILE})

  set(EXTENSION_LICENSE_FILE ${Cjyx_LICENSE_FILE})
  set(EXTENSION_README_FILE ${Cjyx_README_FILE})

  include(CjyxEnableExtensionTesting)
endif()

#-----------------------------------------------------------------------------
# Sources
#-----------------------------------------------------------------------------
set(KIT_PYTHON_SCRIPTS
  MultiVolumeImporter.py
  MultiVolumeImporterPlugin.py
  MultiVolumeImporterLib/__init__.py
  MultiVolumeImporterLib/Helper.py
  )

set(KIT_PYTHON_RESOURCES
  )

#-----------------------------------------------------------------------------
# Build
#-----------------------------------------------------------------------------
ctkMacroCompilePythonScript(
  TARGET_NAME MultiVolumeImporter
  SCRIPTS "${KIT_PYTHON_SCRIPTS}"
  RESOURCES "${KIT_PYTHON_RESOURCES}"
  DESTINATION_DIR ${CMAKE_BINARY_DIR}/${Cjyx_QTSCRIPTEDMODULES_LIB_DIR}
  INSTALL_DIR ${Cjyx_INSTALL_QTSCRIPTEDMODULES_LIB_DIR}
  NO_INSTALL_SUBDIR
  )

#-----------------------------------------------------------------------------
# Testing
#-----------------------------------------------------------------------------
if(BUILD_TESTING)
  add_subdirectory(Testing)
endif()

#-----------------------------------------------------------------------------
# Packaging
#-----------------------------------------------------------------------------
if(NOT Cjyx_SOURCE_DIR)
  include(${Cjyx_EXTENSION_CPACK})
endif()
