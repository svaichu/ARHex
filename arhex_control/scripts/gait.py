#!/usr/bin/env python

import rospy
import math
import angles
import pylab as pl

from std_msgs.msg import Float64
from sensor_msgs.msg import JointState
from math import sin,cos,atan2,sqrt,fabs


#Define a RRBot joint positions publisher for joint controllers.
def arhex_joint_positions_publisher(pub1,pub2,pub3,pub4,pub5,pub6):

    #Initiate node for controlling joint1 and joint2 positions.


    #Define publishers for each joint position controller commands.
    rate = rospy.Rate(100)
    #While loop to have joints follow a certain position, while rospy is not shutdown.
    i = 0
    #stand = 0.01
    #support = angles.pi*40/180
    still = 0
    stand = angles.pi*90/180
    while not rospy.is_shutdown():
        #msg = rospy.wait_for_message('/arhex/joint_states', JointState)
        #stand = angles.pi*90/180
        i = 135
        j = 45.3
        for count in range (0,540):
            if count<270:
                support = angles.pi*i/180
                stand = angles.pi*j/180
                pub1.publish(stand)
                pub2.publish(support)
                pub3.publish(support)
                pub4.publish(stand)
                pub5.publish(stand)
                pub6.publish(support)
                i = i + 1
                j = j + 0.333
                if i == 360:
                    i = 0
                rate.sleep()

            elif count == 270:
                j = 135
                i = 45.3
                support = angles.pi*i/180
                stand = angles.pi*j/180
                pub1.publish(stand)
                pub2.publish(support)
                pub3.publish(support)
                pub4.publish(stand)
                pub5.publish(stand)
                pub6.publish(support)
                j = 136
                i = i + 0.333
                rate.sleep()

            else:
                support = angles.pi*i/180
                stand = angles.pi*j/180
                pub1.publish(stand)
                pub2.publish(support)
                pub3.publish(support)
                pub4.publish(stand)
                pub5.publish(stand)
                pub6.publish(support)
                j = j + 1
                i = i + 0.333
                if j == 360:
                    j = 0
                rate.sleep()



#Main section of code that will continuously run unless rospy receives interuption (ie CTRL+C)
if __name__ == '__main__':
    try:
        rospy.init_node('gait_control_node', anonymous=True)
        pub1 = rospy.Publisher('/arhex/joint1_position_controller/command', Float64, queue_size=10)
        pub2 = rospy.Publisher('/arhex/joint2_position_controller/command', Float64, queue_size=10)
        pub3 = rospy.Publisher('/arhex/joint3_position_controller/command', Float64, queue_size=10)
        pub4 = rospy.Publisher('/arhex/joint4_position_controller/command', Float64, queue_size=10)
        pub5 = rospy.Publisher('/arhex/joint5_position_controller/command', Float64, queue_size=10)
        pub6 = rospy.Publisher('/arhex/joint6_position_controller/command', Float64, queue_size=10)

        #msg = rospy.wait_for_message('/arhex/joint_states', JointState)
        arhex_joint_positions_publisher(pub1,pub2,pub3,pub4,pub5,pub6)
    except rospy.ROSInterruptException: pass
