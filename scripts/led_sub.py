#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def led_callback(msg):

    if msg == a :
        with open("/dev/myled0", "w") as f:
	    f.write("0\n" )

    if msg == b :
        with open("/dev/myled0", "w") as f:
            f.write("1\n" )

    if msg == c :
        with open("/dev/myled0", "w") as f:
            f.write("2\n" )

    if msg == d :
        with open("/dev/myled0", "w") as f:
            f.write("3\n" )

    if msg == e :
        with open("/dev/myled0", "w") as f:
            f.write("R\n" )

if __name__ == "__main__":
        a = Int32(0)
        b = Int32(1)
        c = Int32(2)
        d = Int32(3)
        e = Int32(4)
	rospy.init_node("led_sub")
	sub = rospy.Subscriber("led", Int32, led_callback)
	rospy.spin()
