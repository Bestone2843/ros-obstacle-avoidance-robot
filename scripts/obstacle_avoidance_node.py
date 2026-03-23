#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class ObstacleAvoider:
    def __init__(self):
        rospy.init_node('obstacle_avoidance', anonymous=True)

        self.cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.scan_sub = rospy.Subscriber('/scan', LaserScan, self.scan_callback)

        self.threshold_distance = 0.5  # meters
        self.linear_speed = 0.2
        self.angular_speed = 0.5

        rospy.loginfo("Obstacle Avoidance Node Started")
        rospy.spin()

    def scan_callback(self, scan_data):
        twist = Twist()
        ranges = scan_data.ranges

        # Check front sector (±30 degrees)
        front_ranges = ranges[0:30] + ranges[330:360]
        front_ranges = [r for r in front_ranges if r > 0.1]  # filter invalid

        min_distance = min(front_ranges) if front_ranges else float('inf')

        if min_distance < self.threshold_distance:
            # Obstacle detected — turn
            twist.linear.x = 0.0
            twist.angular.z = self.angular_speed
            rospy.loginfo(f"Obstacle at {min_distance:.2f}m — Turning")
        else:
            # Path clear — move forward
            twist.linear.x = self.linear_speed
            twist.angular.z = 0.0
            rospy.loginfo("Path clear — Moving forward")

        self.cmd_pub.publish(twist)

if __name__ == '__main__':
    try:
        ObstacleAvoider()
    except rospy.ROSInterruptException:
        pass