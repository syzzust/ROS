#!/usr/bin/env python
import rospy
from std_msgs.msg import String
def callback(data):
	print("Received: "+ data.data)
def topic_receive():
	rospy.init_node('topic_receive', anonymous=True)
	rospy.Subscriber('topic_count', String, callback)
	rospy.spin()
if __name__ == '__main__':
	topic_receive()
