from controller import Robot
import math
from controller import Keyboard

# create the Robot instance.
robot = Robot()
keyboard = Keyboard()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# initialize the InertialUnit
inertial_unit = robot.getDevice('inertial unit')

# Enable the InertialUnit
inertial_unit.enable(timestep)

wheel_motor1 = robot.getDevice('motor1')
wheel_motor1.setPosition(float('inf'))
wheel_motor1.setVelocity(0.0)

wheel_motor2 = robot.getDevice('motor2')
wheel_motor2.setPosition(float('inf'))
wheel_motor2.setVelocity(0.0)

wheel_motor3 = robot.getDevice('motor3')
wheel_motor3.setPosition(float('inf'))
wheel_motor3.setVelocity(0.0)

wheel_motor4 = robot.getDevice('motor4')
wheel_motor4.setPosition(float('inf'))
wheel_motor4.setVelocity(0.0)

speed=5

keyboard.enable(timestep)

def move(left_speed,right_speed):
    wheel_motor1.setVelocity(right_speed)
    wheel_motor2.setVelocity(right_speed)  
    wheel_motor3.setVelocity(left_speed)
    wheel_motor4.setVelocity(left_speed)  
            
while robot.step(timestep) != -1:

    if inertial_unit is not None:

        roll_pitch_yaw = inertial_unit.getRollPitchYaw()
            
        # Convert yaw from radians to degrees
        yaw_degrees = math.degrees(roll_pitch_yaw[2])
        
        # Normalize yaw_degrees to be within [0, 360) degrees
        yaw_degrees = yaw_degrees % 360
        if yaw_degrees < 0:
            yaw_degrees += 360
            
        # Print the orientation data
        print(f"Roll: {roll_pitch_yaw[0]}, Pitch: {roll_pitch_yaw[1]}, Yaw: {roll_pitch_yaw[2]}")
        
        # Print the facing direction in degrees
        print(f"Currently facing towards 180 degrees")
    
    key_pressed= keyboard.getKey()
    
    if(key_pressed== 315):
        move(5,5)
        
    if(key_pressed== 317):
        move(-5,-5)
          
    if(key_pressed== 314):
        move(-5,5)
        
    if(key_pressed== 316):
        move(5,-5)
        
    if(key_pressed== -1):
        move(0,0)