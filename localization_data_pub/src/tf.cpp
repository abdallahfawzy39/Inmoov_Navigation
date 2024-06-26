#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from geometry_msgs.msg import TransformStamped
import tf2_ros
import tf

def odom_callback(data):
    # Create a TransformBroadcaster object
    br = tf2_ros.TransformBroadcaster()
    
    # Create a TransformStamped object
    t = TransformStamped()
    
    # Fill in the TransformStamped object
    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "odom"
    t.child_frame_id = "base_link"
    
    # Set the translation
    t.transform.translation.x = data.pose.pose.position.x
    t.transform.translation.y = data.pose.pose.position.y
    t.transform.translation.z = data.pose.pose.position.z
    
    # Set the rotation (quaternion)
    t.transform.rotation = data.pose.pose.orientation
    
    # Send the transform
    br.sendTransform(t)
    
    # Optionally, print the transform for debugging
    rospy.loginfo(t)

def odometry_publisher():
    rospy.init_node('odometry_publisher', anonymous=True)
    
    # Subscribe to the topic publishing the odometry data
    rospy.Subscriber('/robot_pose_ekf/odom_combined', PoseWithCovarianceStamped, odom_callback)
    
    rospy.spin()

if __name__ == '__main__':
    try:
        odometry_publisher()
    except rospy.ROSInterruptException:
        pass

