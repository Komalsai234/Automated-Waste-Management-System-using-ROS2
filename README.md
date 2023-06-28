
# Solid Waste Managament using ROS2

Nowadays, with the rapid increase in the waste generation and raising concern for environmental sustainability, there is requirement for efficient waste management practices. Manual waste sorting and classification processes is highly time consuming task and may lead to health issues for the people involved in the process. To address these problems, this project focuses on developing a waste detection and classification system using ROS2, Tensorflow and Convolution Neural Network (CNN). 

Initially, the project focuses on designing a deep-learning based CNN model which is trained to classify images of waste into organic and recyclable. Using this CNN model, a server-client architecture 
is implemented using ROS2. The client captures the photo of the waste using a webcam and send it to server. The server responds back with the prediction generated by the CNN model.

To validate working of the system in the real world environment, it is simulated in Gazebo simulator with the help of Industrial robot like Panda. This robot with a webcam attached to it, is used to captures the image of the waste. The image is sent to the server for the evaluation; where our CNN model does the prediction. Based upon this prediction, the robot classifies and places it in the desired dustbin.

This approach automates the waste detection and classification process which facilitate the effective waste management practice
and contribution to sustainable environment.


## How to run this Package

- Move into your workspace/src folder
```bash
 $ cd path/to/ros2_ws/src/
  ```


- Clone this repository into you workspace
```bash
 $ git clone https://github.com/Komalsai234/Waste-Segregation-using-ROS2.git
  ```


- Colcon build

```bash
 $ cd .. 

 $ colcon build --package-select my_robot
  ```


- Launch the gazebo file containing robot and the object

```bash
 $ ros2 launch my_robot controller.launch.py
  ```


- Move the robot for taking the photo of object and it in a directory

```bash
 $ ros2 launch my_robot photo.launch.py
  ```

- For requesting the server with the image for prediction, picking and placing the object in their respective bins

```bash
 $ ros2 launch my_robot pick_place.launch.py
  ```

## Gazebo Simulation

https://github.com/Komalsai234/Waste-Segregation-using-ROS2/assets/99163734/fabde290-824a-4a4c-80e2-5d0a1ec6fafe




## Package Dependencies
- Tensorflow 2.9.0
- Open CV
- cv_bridge
- effort_controllers
- gazebo_plugins
- gazebo_ros2_control
- gazebo_ros_pkgs
- joint_state_broadcaster
- joint_state_publisher
- joint_state_publisher_gui
- joint_trajectory_controller



## System Requirment

- Ubuntu 22.04.02
- ROS2 Humble
- Gazebo 11

## Instructor

### Dr. Navaneeth Haridasan, Assistant Professor, Center for Computational Engineering and Networking (CEN)


## Contributors

- [P.S.S.Sai Keerthana](https://github.com/saikeerthana234)
- [P. Komal Sai Anurag](https://www.github.com/komalsai234)
- [Udayagiri Varun](https://github.com/VarunUdayagiri)
- [Sejal Singh](https://github.com/sejal923)

