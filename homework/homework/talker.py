import rclpy
from rclpy.node import Node
from project_msgs.msg import Project

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Project, "project", 10)
n = 0


def cb():
    global n
    msg = Project()
    msg.name = "廣原灯"
    msg.age = n
    pub.publish(msg)
    n += 1


def main():
    node.create_timer(0.5, cb)
    rclpy.spin(node)
