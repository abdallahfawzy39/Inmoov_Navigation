#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def callback(data):
    pub.publish(data)

if __name__ == '__main__':
    rospy.init_node('topic_remapper', anonymous=True)
    rospy.Subscriber('/diff_drive_controller/cmd_vel', Twist, callback)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.spin()

