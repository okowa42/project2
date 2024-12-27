import rclpy
from rclpy.node import Node
from project_msgs.msg import Project


rclpy.init()
node = Node("listener")


def cb(msg):
    global node
    node.get_logger().info("Listen: %s" % msg)


def main():
    pub = node.create_subscription(Project, "project", cb, 10)
    rclpy.spin(node)
