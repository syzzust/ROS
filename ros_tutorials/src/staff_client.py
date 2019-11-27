#!/usr/bin/env python
import rospy
import sys
from ros_basics.srv import *
def staff_client():
    rospy.init_node('staff_client', anonymous=True)
    rospy.wait_for_service('staff_req')
    get_staff_info = rospy.ServiceProxy('staff_req', MyStaff)
    while not rospy.is_shutdown():
        req_name = raw_input("Please input name:")
        resp = get_staff_info(req_name)
        print("Gender:%s, Age:%d, Duty:%s" % (resp.gender, resp.age, resp.duty))
if __name__ == '__main__':
    staff_client()
