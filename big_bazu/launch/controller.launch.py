import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    urdf = '/home/hp/ros2_ws/src/my_robot/urdf/my_robot.urdf'
    urdf_file = '/home/hp/ros2_ws/src/my_robot/urdf/coke_can.urdf'
    urdf_bin = '/home/hp/ros2_ws/src/my_robot/urdf/bin.urdf'
    urdf_org = '/home/hp/ros2_ws/src/my_robot/urdf/organic.urdf'

    with open(urdf, 'r') as infp:
        robot_desc = infp.read()
        
    with open(urdf_file, 'r') as infp:
        coke_tin = infp.read()
        
    with open(urdf_bin, 'r') as infp:
        bin_rec = infp.read()
        
    with open(urdf_org, 'r') as infp:
        bin_organic = infp.read()

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_desc}],
            arguments=[urdf]
        ),

        # Gazebo related stuff required to launch the robot in simulation
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            output='screen',
            arguments=["-topic", "/robot_description", "-entity", "gripper_robot"]
        ),

        Node(
            package="gazebo_ros",
            executable="spawn_entity.py",
            arguments=["-entity", "coke_can_model", "-b", "-file", urdf_file]
        ),
        
        Node(
            package="gazebo_ros",
            executable="spawn_entity.py",
            arguments=["-entity", "bin", "-b", "-file", urdf_bin]
        ),
        
        Node(
            package="gazebo_ros",
            executable="spawn_entity.py",
            arguments=["-entity", "organic", "-b", "-file", urdf_org]
        ),

        # Running the controllers in launch file
        ExecuteProcess(
            cmd=['ros2', 'control', 'load_controller', '--set-state', 'active', 'joint_state_broadcaster'],
            output='screen'
        ),

        ExecuteProcess(
            cmd=['ros2', 'control', 'load_controller', '--set-state', 'active', 'joint_trajectory_controller'],
            output='screen'
        )
    ])

