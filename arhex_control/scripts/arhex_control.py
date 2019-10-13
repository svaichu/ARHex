#!/usr/bin/env python

import rospy
import math

from std_msgs.msg import Float64
from math import sin,cos,atan2,sqrt,fabs

#Define a RRBot joint positions publisher for joint controllers.
def arhex_joint_positions_publisher():

    #Initiate node for controlling joint1 and joint2 positions.
    rospy.init_node('joint_positions_node', anonymous=True)

    #Define publishers for each joint position controller commands.
    pub1 = rospy.Publisher('/arhex/joint1_position_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/arhex/joint2_position_controller/command', Float64, queue_size=10)
    pub3 = rospy.Publisher('/arhex/joint3_position_controller/command', Float64, queue_size=10)
    pub4 = rospy.Publisher('/arhex/joint4_position_controller/command', Float64, queue_size=10)
    pub5 = rospy.Publisher('/arhex/joint5_position_controller/command', Float64, queue_size=10)
    pub6 = rospy.Publisher('/arhex/joint6_position_controller/command', Float64, queue_size=10)
    rate = rospy.Rate(200)
    #While loop to have joints follow a certain position, while rospy is not shutdown.
    i = 0
    while not rospy.is_shutdown():

        #Have each joint follow a sine movement of sin(i/100).
        cir_movement = (i/100.)
        cir_off_movement = ((i/100.)+185.5)
        #Publish the same sine movement to each joint.
        pub1.publish(cir_movement)
        pub2.publish(cir_off_movement)
        pub3.publish(cir_off_movement)
        pub4.publish(cir_movement)
        pub5.publish(cir_movement)
        pub6.publish(cir_off_movement)

        i = i+1 #increment i

        rate.sleep() #sleep for rest of rospy.Rate(100)

#Main section of code that will continuously run unless rospy receives interuption (ie CTRL+C)
if __name__ == '__main__':
    try: arhex_joint_positions_publisher()
    except rospy.ROSInterruptException: pass