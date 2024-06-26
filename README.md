Rplidar : lidar driver package. 
Main_package: includes launch files for our project. Including gmap, hector, navigation_stack, some trials. 
mpu6050: Imu driver package.
Hector: hector slam for mapping package. 
Localization_data_pub: include a node that turn wheel encoders to odometry and another for subscribing to initial and goal position on rviz. 
Robot_pose_ekf: for sensor fusion between lidar and imu. 
Navstack_pub: parameters of navigation stack including planners, global and local costmaps, etc. 
urdf12: includes urdf model for our robot’s visualization (Gazebo and RVIZ)
rosserial: enable microcontrollers to communicate with ros.

(Rplidar, mpu6050_driver, Hector, rosserial and Robot_pose_ekf packages were downloaded from Github and implemented in our project)
