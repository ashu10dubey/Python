#!/usr/bin/env python3

import rospy
from your_package_name.msg import Sample  # Update with your package name and message type

def publisher():
    rospy.init_node('sample_publisher', anonymous=True)
    pub = rospy.Publisher('sample_topic', Sample, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        name = input("Enter student name: ")
        roll_no = int(input("Enter roll number: "))
        marks = float(input("Enter marks: "))

        msg = Sample()
        msg.name = name
        msg.roll_no = roll_no
        msg.marks = marks

        rospy.loginfo("Publishing: %s, %d, %.2f", msg.name, msg.roll_no, msg.marks)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass