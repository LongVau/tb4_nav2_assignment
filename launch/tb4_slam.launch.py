from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    tb4_ignition = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            FindPackageShare('turtlebot4_ignition_bringup'), '/launch/turtlebot4_ignition.launch.py'
        ]),
        launch_arguments={
            'world': 'maze',
            'model': 'standard',
            'slam': 'true',
            'rviz': 'true',
            'headless': 'false'
        }.items()
    )
    return LaunchDescription([tb4_ignition])
