#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped

# Node initialization
rospy.init_node('init_pose')
pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size=1)

# Construct message
init_msg = PoseWithCovarianceStamped()
init_msg.header.frame_id = "map"

# Set initial pose to (0, 0, 0) for position and (0, 0, 0, 1) for orientation
init_msg.pose.pose.position.x = 0.0
init_msg.pose.pose.position.y = 0.0
init_msg.pose.pose.position.z = 0.0
init_msg.pose.pose.orientation.x = 0.0
init_msg.pose.pose.orientation.y = 0.0
init_msg.pose.pose.orientation.z = 0.0
init_msg.pose.pose.orientation.w = 1.0

# Delay
rospy.sleep(1)

# Publish message
rospy.loginfo("setting initial pose to (0, 0, 0) position and (0, 0, 0, 1) orientation")
pub.publish(init_msg)
rospy.loginfo("initial pose is set")

