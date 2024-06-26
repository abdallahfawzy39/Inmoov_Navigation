#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Imu
from tf.transformations import euler_from_quaternion, quaternion_from_euler

def imu_callback(data):
    # Extract the quaternion orientation
    quat = (
        data.orientation.x,
        data.orientation.y,
        data.orientation.z,
        data.orientation.w
    )

    # Convert quaternion to Euler angles
    roll, pitch, yaw = euler_from_quaternion(quat)

    # Modify the yaw (divide by 2)
    new_yaw = yaw / 2

    # Convert Euler angles back to quaternion
    new_quat = quaternion_from_euler(roll, pitch, new_yaw)

    # Create a new Imu message with the modified orientation
    new_data = Imu()
    new_data.header = data.header
    new_data.orientation.x = new_quat[0]
    new_data.orientation.y = new_quat[1]
    new_data.orientation.z = new_quat[2]
    new_data.orientation.w = new_quat[3]
    new_data.orientation_covariance = data.orientation_covariance
    new_data.angular_velocity = data.angular_velocity
    new_data.angular_velocity_covariance = data.angular_velocity_covariance
    new_data.linear_acceleration = data.linear_acceleration
    new_data.linear_acceleration_covariance = data.linear_acceleration_covariance
    
    # Publish the modified IMU data
    imu_pub.publish(new_data)

def imu_listener():
    rospy.init_node('imu_listener', anonymous=True)

    # Subscribe to the IMU topic
    rospy.Subscriber("/imu/data_filtered", Imu, imu_callback)

    # Create a publisher for the modified IMU data
    global imu_pub
    imu_pub = rospy.Publisher('/modified_imu_topic', Imu, queue_size=10)

    # Spin to keep the script from exiting
    rospy.spin()

if __name__ == '__main__':
    try:
        imu_listener()
    except rospy.ROSInterruptException:
        pass

