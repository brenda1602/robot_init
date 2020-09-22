import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, ThisLaunchFileDir
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    pkg_robot_gazebo= get_package_share_directory('robot_gazebo')
    pkg_robot_description= get_package_share_directory('description')
    urdf=os.path.join(pkg_robot_description,'src', 'urdf', 'robot.urdf')
    urdf_file= LaunchConfiguration('urdf_file')
    #urdf = (urdf.read())
    assert urdf

      # Gazebo launch
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_robot_gazebo, 'launch', 'gazebo.launch.py'),
        )
    )

    return LaunchDescription(
        [
            Node(
                package='robot_state_publisher',
                node_executable='robot_state_publisher',
                node_name='robot_state_publisher',
                output='screen',
                arguments=[(urdf)]
            ),
            gazebo,
            DeclareLaunchArgument(name='robot', default_value=urdf,
                                                description='Absolute path to robot urdf file'),
        ]
    )
        