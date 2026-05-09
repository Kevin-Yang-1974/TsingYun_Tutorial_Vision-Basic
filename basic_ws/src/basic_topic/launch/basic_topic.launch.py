from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='basic_topic',
            executable='publisher_component_node',
            name='publisher_component_node',
            output='screen'
        ),
        Node(
            package='basic_topic',
            executable='subscriber_component_node',
            name='subscriber_component_node',
            output='screen'
        )
    ])
    pass