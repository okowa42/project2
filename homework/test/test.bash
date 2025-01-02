#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch homework bitcoin_publisher.py > /tmp/homework.log

cat /tmp/homework.log |
grep 'Bitcoin price:'
