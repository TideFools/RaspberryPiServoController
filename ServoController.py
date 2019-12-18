#!/usr/bin/env python3

## Authors: Sean McAtee, Merai Dandouch
## Version: 12/17/2019

## About:
#       This program is for a Raspberry Pi connected to an Adafruit Driver 
#       to control the speed of 12 servo motors.

## Hardware:
#   Pi: Raspberry Pi 3 Model B
#   OS: Raspbian Buster Lite (Version: September 2019)
#   Driver: Adafruit CA9685 16-Channel 12-Bit PWM Driver

## Dependencies:
#   RPI.GPIO
#   python-smbus
#   Adafruit_PCA9685
#       https://github.com/adafruit/Adafruit_Python_PCA9685


from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685

#Uncomment for debug output
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (address=0x40) and bus
pwm = Adafruit_PCA9685.PCA9685()

# Configure min and max servo pulse lengths
#   pulse length out of 4096
#   0-4 stop servos
#   ~300 to 350 modulate speed clockwise
#   ~354 to 430 modulate speed counterclockwise
servo_min = 300  # Min pulse length out of 4096
servo_max = 430  # Max pulse length out of 4096

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

print('Moving all servos, press Ctrl-C to quit...')

# Moves all servos through functional range of pulse lengths
i = servo_min
while i <= servo_max:
    pwm.set_all_pwm(0, i)
    print(i)
    time.sleep(0.1)
    i = i + 1

#stop servos with pulse 350
pwm.set_all_pwm(0, 0)