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
    urdf_file=os.path.join(pkg_robot_description,'src', 'urdf', 'robot.urdf')
    urdf = open(urdf_file).read()

    #gazebo launch
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([ThisLaunchFileDir(), '/gazebo.launch.py']),
             )
    spawn_entity = Node(package='gazebo_ros', node_executable='spawn_entity.py',
                        arguments=['-entity', 'demo', '-database', 'double_pendulum_with_base'],
                        output='screen')

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation (Gazebo) clock if true'),

        Node(
            package='robot_state_publisher',
            node_executable='robot_state_publisher',
            node_name='robot_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time}],
            arguments=[urdf_file]),
        spawn_entity,
        gazebo,
    ])
          #  DeclareLaunchArgument(
       #     'world',
        #    default_value=[os.path.join(pkg_robot_gazebo, 'src','worlds', 'empty.world'), ''],
         #   description='empty world'
       # ),