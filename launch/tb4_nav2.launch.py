import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    pkg_share = get_package_share_directory('tb4_nav2_assignment')
    map_file = os.path.join(pkg_share, 'maps', 'map.yaml')

    tb4_nav = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            FindPackageShare('turtlebot4_ignition_bringup'), '/launch/turtlebot4_ignition.launch.py'
        ]),
        launch_arguments={
            'world': 'maze',
            'model': 'standard',
            'nav2': 'true',
            'slam': 'false',
            'localization': 'true',
            'rviz': 'true',
            'map': map_file,
            'headless': 'false',
        }.items()
    )
    return LaunchDescription([tb4_nav])
