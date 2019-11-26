#!/usr/bin/env python
import rospy
from ros_basics.msg import MyPoint
def callback(data):
	print("Received Point: x=%f, y=%f" % (data.x, data.y))
def topic_receive_msg():
	rospy.init_node('topic_receive', anonymous=True)
	rospy.Subscriber('topic_pos', MyPoint, callback)
	rospy.spin()
if __name__ == '__main__':
	topic_receive_msg()
