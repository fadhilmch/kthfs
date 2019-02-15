#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String


def broadcast():
    # Initialize as publisher for topic 'mochammad'
    pub = rospy.Publisher('mochammad', String, queue_size=10)
    #Initialize as node 'broadcast_node'
    rospy.init_node('broadcast_node', anonymous=True)
    #Set the broadcast rate to 0.05
    rate = rospy.Rate(0.5)
    k = 1
    while not rospy.is_shutdown():
        rospy.loginfo(k)
        pub.publish(str(k))
        k += 4
        rate.sleep()

if __name__ == '__main__':
    try:
        broadcast()
    except rospy.ROSInterruptException:
        pass
