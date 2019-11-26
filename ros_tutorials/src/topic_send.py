#!/usr/bin/env python
import rospy
from std_msgs.msg import String
def topic_send():
	rospy.init_node('topic_send', anonymous=True)
	pub = rospy.Publisher('topic_count', String, queue_size=10)
	rate = rospy.Rate(1)
	count = 0
	while not rospy.is_shutdown():
		topic_str = "Topic Send: %d" % count
		count += 1
		pub.publish(topic_str)
		rate.sleep()
if __name__ == '__main__':
	try:
		topic_send()
	except rospy.ROSInterruptException:
		pass
