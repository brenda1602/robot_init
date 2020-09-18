import os 
import sys

from ament_index_python.packages import get_package_share_directory 

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription 
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir, LaunchConfiguration


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    pkg_robot_gazebo= get_package_share_directory('robot_gazebo')
    pkg_robot_description= get_package_share_directory('description')
    urdf_file=os.path.join(pkg_robot_description,'src', 'urdf', 'robot.urdf')
    urdf = open(urdf_file).read()

    #gazebo launch
    gazebo=IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros,'launch', 'gazebo.launch.py'),
        )
    )
          
    
    return LaunchDescription([
        DeclareLaunchArgument(
           'use_sim_time',
           default_value=use_sim_time,
           description='Use simulation (Gazebo) clock if true'),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [ThisLaunchFileDir(), '/state.launch.py']),
            launch_arguments={'use_sim_time': use_sim_time}.items(),
        ),

        gazebo,

        Node(
            package='robot_state_publisher',
            node_executable='robot_state_publisher',
            node_name='robot_state_publisher',
            output='screen',
            
            ),
        
    ])