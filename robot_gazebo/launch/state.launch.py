import os
from pathlib import Path

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, ThisLaunchFileDir
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():

   
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    pkg_robot_gazebo= FindPackageShare('robot_gazebo').find('robot_gazebo')
    pkg_robot_description= FindPackageShare('description').find('robot_gazebo')
    urdf=os.path.join(pkg_robot_description,'src', 'urdf', 'robot.urdf')
    urdf_file= LaunchConfiguration('urdf_file')
    #urdf = (urdf.read())
    assert urdf

      # Gazebo launch
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([ThisLaunchFileDir(), '/gazebo.launch.py']),
             )

    spawn_entity = Node(package='gazebo_ros', node_executable='spawn_entity.py',
                        arguments=['-entity', 'demo', '-database', ],
                        output='screen')

    return LaunchDescription(
        [
            Node(
                package='robot_state_publisher',
                node_executable='robot_state_publisher',
                output='screen',
                arguments=[(urdf)]
            ),
            DeclareLaunchArgument('urdf_file',
                default_value=(urdf),
                description='Absolute path to robot urdf file'
            ),
            DeclareLaunchArgument(
            'world',
            default_value=[os.path.join(pkg_robot_gazebo, 'worlds', 'empty_world.world'), ''],
            description='SDF world file'
            ),
            spawn_entity
        ]
    )
        