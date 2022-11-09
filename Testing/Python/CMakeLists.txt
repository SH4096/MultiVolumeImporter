set(KIT_UNITTEST_SCRIPTS)
CjyxMacroConfigureGenericPythonModuleTests("${EXTENSION_NAME}" KIT_UNITTEST_SCRIPTS)

foreach(script_name ${KIT_UNITTEST_SCRIPTS})
  cjyx_add_python_unittest(
    SCRIPT ${script_name}
    CJYX_ARGS --no-main-window --disable-cli-module TESTNAME_PREFIX nomainwindow_)
endforeach()

