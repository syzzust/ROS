#!/usr/bin/env python
import rospy
from ros_basics.srv import MyStaff, MyStaffResponse
staff_info={'John':['M',45,'Manager'], 'Mary':['F',25,'Secretary'], 'Tod':['M',32,'Worker']}
def Querry_Staff(req):
    staff = staff_info[req.name]
    resp = MyStaffResponse( gender=staff[0], age=staff[1], duty=staff[2])
    return resp
def staff_server():
    rospy.init_node('staff_server', anonymous=True)
    service = rospy.Service('staff_req', MyStaff, Querry_Staff)
    rospy.spin()
if __name__ == '__main__':
    staff_server()
