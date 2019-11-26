#!/usr/bin/env python
import rospy
import random
from ros_basics.msg import MyPoint 
def topic_send_msg():
	rospy.init_node('topic_send_msg', anonymous=True)
	pub = rospy.Publisher('topic_pos', MyPoint, queue_size=10)
	rate = rospy.Rate(1)
	point=MyPoint()
	while not rospy.is_shutdown():
		point.x = random.random()
		point.y = random.random()
		pub.publish(point)
		rate.sleep()
if __name__ == '__main__':
	try:
		topic_send_msg()
	except rospy.ROSInterruptException:
		pass
