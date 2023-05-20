# Import the necessary Webots libraries
from controller import Robot, Motor, TouchSensor

# Create an instance of the Robot class
robot = Robot()

# Get handles to the robot's motors and touch sensors
lf_motor = robot.getDevice("right_wheel")
rt_motor = robot.getDevice("left_wheel")

ds_left = robot.getDevice("left_ts")
ds_right = robot.getDevice("right_ts")
ds_cent = robot.getDevice("center_ts")

ds_left.enable(64)
ds_right.enable(64)
ds_cent.enable(64)

# Set the velocity of the motors
lf_motor.setPosition(float('inf'))
rt_motor.setPosition(float('inf'))

# Set initial velocity
velocity = 1.2
