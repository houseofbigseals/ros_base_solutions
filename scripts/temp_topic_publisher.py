#! /usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import Float32

rospy.init_node('temp_publisher')
pub = rospy.Publisher('/cpu_temp', Float32, queue_size=1)
freq = rospy.get_param("~pub_freq", default=1)
rate = rospy.Rate(freq)
temp = Float32()

def getCPUTemp():
    data = open('/sys/class/thermal/thermal_zone0/temp', 'r').read()
    return round(float(int(data)/1000.0),1)

while not rospy.is_shutdown():
    temp.data = getCPUTemp()
    pub.publish(temp)
    rate.sleep()

