# ROS Obstacle Avoidance Robot

## Overview
This project implements a ROS-based obstacle avoidance system using LiDAR data in Gazebo simulation.

The robot subscribes to `/scan` data and publishes velocity commands to `/cmd_vel` to navigate autonomously.

## Tools Used
- ROS (Noetic / ROS2 Humble)
- Gazebo Simulator
- TurtleBot3
- Python

## Algorithm
1. Read LiDAR scan data
2. Detect obstacles within threshold distance
3. Adjust angular velocity
4. Continue forward motion if path is clear

## Demo
(Add video link)

## How to Run

```bash
roslaunch obstacle_avoidance simulation.launch