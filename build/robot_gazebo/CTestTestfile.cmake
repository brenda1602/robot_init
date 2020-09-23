# CMake generated Testfile for 
# Source directory: /home/brenda/RBIM_ws/src/robot_gazebo
# Build directory: /home/brenda/RBIM_ws/src/build/robot_gazebo
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(copyright "/usr/bin/python3" "-u" "/opt/ros/eloquent/share/ament_cmake_test/cmake/run_test.py" "/home/brenda/RBIM_ws/src/build/robot_gazebo/test_results/robot_gazebo/copyright.xunit.xml" "--package-name" "robot_gazebo" "--output-file" "/home/brenda/RBIM_ws/src/build/robot_gazebo/ament_copyright/copyright.txt" "--command" "/opt/ros/eloquent/bin/ament_copyright" "--xunit-file" "/home/brenda/RBIM_ws/src/build/robot_gazebo/test_results/robot_gazebo/copyright.xunit.xml")
set_tests_properties(copyright PROPERTIES  LABELS "copyright;linter" TIMEOUT "60" WORKING_DIRECTORY "/home/brenda/RBIM_ws/src/robot_gazebo")
add_test(flake8 "/usr/bin/python3" "-u" "/opt/ros/eloquent/share/ament_cmake_test/cmake/run_test.py" "/home/brenda/RBIM_ws/src/build/robot_gazebo/test_results/robot_gazebo/flake8.xunit.xml" "--package-name" "robot_gazebo" "--output-file" "/home/brenda/RBIM_ws/src/build/robot_gazebo/ament_flake8/flake8.txt" "--command" "/opt/ros/eloquent/bin/ament_flake8" "--xunit-file" "/home/brenda/RBIM_ws/src/build/robot_gazebo/test_results/robot_gazebo/flake8.xunit.xml")
set_tests_properties(flake8 PROPERTIES  LABELS "flake8;linter" TIMEOUT "60" WORKING_DIRECTORY "/home/brenda/RBIM_ws/src/robot_gazebo")
add_test(lint_cmake "/usr/bin/python3" "-u" "/opt/ros/eloquent/share/ament_cmake_test/cmake/run_test.py" "/home/brenda/RBIM_ws/src/build/robot_gazebo/test_results/robot_gazebo/lint_cmake.xunit.xml" "--package-name" "robot_gazebo" "--output-file" "/home/brenda/RBIM_ws/src/build/robot_gazebo/ament_lint_cmake/lint_cmake.txt" "--command" "/opt/ros/eloquent/bin/ament_lint_cmake" "--xunit-file" "/home/brenda/RBIM_ws/src/build/robot_gazebo/test_results/robot_gazebo/lint_cmake.xunit.xml")
set_tests_properties(lint_cmake PROPERTIES  LABELS "lint_cmake;linter" TIMEOUT "60" WORKING_DIRECTORY "/home/brenda/RBIM_ws/src/robot_gazebo")
add_test(pep257 "/usr/bin/python3" "-u" "/opt/ros/eloquent/share/ament_cmake_test/cmake/run_test.py" "/home/brenda/RBIM_ws/src/build/robot_gazebo/test_results/robot_gazebo/pep257.xunit.xml" "--package-name" "robot_gazebo" "--output-file" "/home/brenda/RBIM_ws/src/build/robot_gazebo/ament_pep257/pep257.txt" "--command" "/opt/ros/eloquent/bin/ament_pep257" "--xunit-file" "/home/brenda/RBIM_ws/src/build/robot_gazebo/test_results/robot_gazebo/pep257.xunit.xml")
set_tests_properties(pep257 PROPERTIES  LABELS "pep257;linter" TIMEOUT "60" WORKING_DIRECTORY "/home/brenda/RBIM_ws/src/robot_gazebo")
add_test(xmllint "/usr/bin/python3" "-u" "/opt/ros/eloquent/share/ament_cmake_test/cmake/run_test.py" "/home/brenda/RBIM_ws/src/build/robot_gazebo/test_results/robot_gazebo/xmllint.xunit.xml" "--package-name" "robot_gazebo" "--output-file" "/home/brenda/RBIM_ws/src/build/robot_gazebo/ament_xmllint/xmllint.txt" "--command" "/opt/ros/eloquent/bin/ament_xmllint" "--xunit-file" "/home/brenda/RBIM_ws/src/build/robot_gazebo/test_results/robot_gazebo/xmllint.xunit.xml")
set_tests_properties(xmllint PROPERTIES  LABELS "xmllint;linter" TIMEOUT "60" WORKING_DIRECTORY "/home/brenda/RBIM_ws/src/robot_gazebo")