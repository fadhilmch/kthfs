#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + " Data: %s", data.data)
    temp = int(data.data)*0.15
    pub = rospy.Publisher('result', String, queue_size=10)
    rospy.loginfo("Publish: "+ str(temp))
    pub.publish(str(temp))


def listener():
    rospy.init_node('nodeB', anonymous=True)

    rospy.Subscriber("mochammad", String, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
