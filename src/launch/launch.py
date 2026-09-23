"""

Copyright (c) 2023 Kieran Aponte
This software is licensed under the MIT License.

"""

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.substitutions import TextSubstitution
from launch_ros.actions import Node
def generate_launch_description():

    ign_model_prefix = '/model/' + 'kora'
    #background_r_launch_arg = DeclareLaunchArgument(
    #    "background_r", default_value=TextSubstitution(text="0")
    #)

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    #testing = LaunchConfiguration('testing', default='0')
    pkg_name = 'kora'
    urdf_file_name = 'kora_desc/kora.urdf'

    urdf = os.path.join(
        get_package_share_directory('kora'),
        urdf_file_name)
    with open(urdf, 'r') as infp:
        robot_desc = infp.read()
    
    Robot_State_Publisher = Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time, 'robot_description': robot_desc}],
            arguments=[urdf])
    
    Kora_State_Publisher = Node(
            package='kora',
            executable='state_publisher.py',
            name='state_publisher',
            output='screen')
    #ros_ign redirects to ros_gz so generally just use ros_gz. source: https://github.com/gazebosim/ros_gz
    Color_Bridge = Node(
        package='ros_gz_bridge', #[parameter_bridge-3] [ros_ign_bridge] is deprecated! Redirecting to use [ros_gz_bridge] instead!
        executable='parameter_bridge',
        name='parameter_bridge',
        output='screen',
        parameters=[{'use_sim_time': use_sim_time
			}],
        #arguments=['/model/kora/color_camera@sensor_msgs/msg/Image@ignition.msgs.Image'])
        arguments=['/world/kora_world/model/kora/link/realsense/sensor/camera_sensor_color/image@sensor_msgs/msg/Image[ignition.msgs.Image'],
        remappings = [('/world/kora_world/model/kora/link/realsense/sensor/camera_sensor_color/image', '/camera/image')])
    
    Depth_Bridge = Node( # PointCloudPacked -> PointCloud2 is correct: https://index.ros.org/p/ros_gz_bridge/#humble
        package='ros_gz_bridge',
        executable='parameter_bridge',
        name='parameter_bridge',
        output='screen',
        parameters=[{'use_sim_time': use_sim_time}],
        arguments=['/world/kora_world/model/kora/link/realsense/sensor/depth_sensor/depth_image/points@sensor_msgs/msg/PointCloud2[ignition.msgs.PointCloudPacked'],
        remappings = [
				('/world/kora_world/model/kora/link/realsense/sensor/depth_sensor/depth_image/points', '/depth_camera/points')])    
    '''Depth_Bridge2 = Node(
        package='ros_gz_bridge', 
        executable='parameter_bridge',
        name='parameter_bridge',
        output='screen',
        parameters=[{'use_sim_time': use_sim_time}],
        arguments=['/world/kora_world/model/kora/link/realsense/sensor/depth_camera_front/depth_image/points@sensor_msgs/msg/PointCloud2@ignition.msgs.PointCloudPacked'],
        remappings = [
				('/world/kora_world/model/kora/link/realsense/sensor/depth_camera_front/depth_image/points', '/depth_camera2/points')])
    '''
    '''
    RealSense = Node(
        package='realsense2_camera',
        executable='realsense2_camera_node',
        name='realsense2_node',
        output='screen')
    ''' 
    
    Launch_Arg = DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation (Gazebo) clock if true')
    
    Test_Arg = DeclareLaunchArgument(
        'testing',
        default_value = '0',
        description='dummy argument'
    )
    

    return LaunchDescription([Launch_Arg, Robot_State_Publisher, Kora_State_Publisher, Color_Bridge, Depth_Bridge])

        

    '''
        Node(package='ros_ign_bridge', executable='parameter_bridge',
			namespace = 'kora',
			name = 'depth_camera_bridge',
			output='screen',
			parameters=[{
				'use_sim_time': use_sim_time
			}],
			arguments = [
				 ign_model_prefix + '/depth_camera' + '@sensor_msgs/msg/Image' + '[ignition.msgs.Image',
				 ign_model_prefix + '/depth_camera/points' + '@sensor_msgs/msg/PointCloud2' + '@ignition.msgs.PointCloudPacked'
			],
			remappings = [
				(ign_model_prefix + '/depth_camera', '/depth_camera'),
				(ign_model_prefix + '/depth_camera/points', '/depth_camera/points')
			])'''
    #])
        

        
        
    
