import rospy
from geometry_msgs.msg import Twist
import math

def draw_shape(n, side_length):
    # Initialize the node
    rospy.init_node('draw_shape_node', anonymous=True)
    # Create a publisher for sending commands to the turtle
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    # Create a Twist message
    move_cmd = Twist()

    # Calculate the angle between lines
    angle = 360 / n

    # Loop to draw the shape
    for _ in range(n+1):
        # Move forward
        move_cmd.linear.x = side_length
        move_cmd.angular.z = 0
        pub.publish(move_cmd)
        rospy.sleep(1)  # Adjust the sleep time as needed

        # Turn
        move_cmd.linear.x = 0
        move_cmd.angular.z = math.radians(angle)  # Convert degrees to radians
        pub.publish(move_cmd)
        rospy.sleep(1)  # Adjust the sleep time as needed

    # Stop the turtle
    move_cmd.linear.x = 0
    move_cmd.angular.z = 0
    pub.publish(move_cmd)

if __name__ == '__main__':
    try:
        # Specify the number of sides and side length
        num_sides = 4
        side_length = 2

        # Draw the shape
        draw_shape(num_sides, side_length)
    except rospy.ROSInterruptException:
        pass