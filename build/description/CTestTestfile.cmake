# CMake generated Testfile for 
# Source directory: /home/brenda/RBIM_ws/src/description
# Build directory: /home/brenda/RBIM_ws/src/build/description
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(lint_cmake "/usr/bin/python3" "-u" "/opt/ros/eloquent/share/ament_cmake_test/cmake/run_test.py" "/home/brenda/RBIM_ws/src/build/description/test_results/description/lint_cmake.xunit.xml" "--package-name" "description" "--output-file" "/home/brenda/RBIM_ws/src/build/description/ament_lint_cmake/lint_cmake.txt" "--command" "/opt/ros/eloquent/bin/ament_lint_cmake" "--xunit-file" "/home/brenda/RBIM_ws/src/build/description/test_results/description/lint_cmake.xunit.xml")
set_tests_properties(lint_cmake PROPERTIES  LABELS "lint_cmake;linter" TIMEOUT "60" WORKING_DIRECTORY "/home/brenda/RBIM_ws/src/description")
add_test(xmllint "/usr/bin/python3" "-u" "/opt/ros/eloquent/share/ament_cmake_test/cmake/run_test.py" "/home/brenda/RBIM_ws/src/build/description/test_results/description/xmllint.xunit.xml" "--package-name" "description" "--output-file" "/home/brenda/RBIM_ws/src/build/description/ament_xmllint/xmllint.txt" "--command" "/opt/ros/eloquent/bin/ament_xmllint" "--xunit-file" "/home/brenda/RBIM_ws/src/build/description/test_results/description/xmllint.xunit.xml")
set_tests_properties(xmllint PROPERTIES  LABELS "xmllint;linter" TIMEOUT "60" WORKING_DIRECTORY "/home/brenda/RBIM_ws/src/description")
