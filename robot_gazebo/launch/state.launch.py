 
# Copyright 2019 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Demo for spawn_entity.
Launches Gazebo and spawns a model
"""
import os
from pathlib import Path

from ament_index_python.packages import get_package_share_directory

import xacro 

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, ExecuteProcess,  SetEnvironmentVariable
from launch.substitutions import LaunchConfiguration, ThisLaunchFileDir
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():

   
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    pkg_robot_gazebo= FindPackageShare('robot_gazebo').find('robot_gazebo')
    pkg_robot_description= FindPackageShare('description').find('description')
    xacro_file=os.path.join(pkg_robot_description,'src', 'urdf', 'robot.xacro')
    doc=xacro.process_file(xacro_file)
    urdf= os.path.join(pkg_robot_description,'src', 'urdf', 'robot.urdf')
    arguments=os.path.join(pkg_robot_description,'src', 'urdf', 'robot.xacro')

    robot_desc = doc.toprettyxml(indent='  ')
    robot_desc = robot_desc.replace('"', '\\"')
    spawn_args = '{name: \"robot\", xml: \"'  +  robot_desc + '\"}'
   
    config=os.path.join(pkg_robot_gazebo,'plugins','move_config.yaml')

      # Gazebo launch
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([ThisLaunchFileDir(), '/gazebo.launch.py']),
             )

    spawn_entity = ExecuteProcess(
            cmd=['ros2', 'service', 'call', '/spawn_entity', 'gazebo_msgs/SpawnEntity', spawn_args],
            output='screen')

    rviz = Node(
        package='rviz2',
        node_executable='rviz2',
        arguments=['-d', os.path.join(pkg_robot_gazebo,'rviz','default.rviz')],
    )

    return LaunchDescription(
        [   
            gazebo,
            spawn_entity,
            Node(
                package='joint_state_publisher',
                node_executable='joint_state_publisher',
                arguments=[str(xacro_file)]),   
            DeclareLaunchArgument('rviz', default_value='true',
                              description='Open RViz.'),        
            rviz
        ])
        