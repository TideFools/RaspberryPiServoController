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

#Debug output
import logging
logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685
#   using the default address (address=0x40)
#   using the default bus (busnum=1)
pwm = Adafruit_PCA9685.PCA9685()

# Configure min and max servo pulse lengths
servo_min = 348  # Min pulse length out of 4096
servo_max = 351  # Max pulse length out of 4096
servo_stop = 350 # Holds servo in idle

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

print('Moving servo on channel 0, press Ctrl-C to quit...')
i = 0
while i < 3:
    # Move servo on channel O between extremes.
    pwm.set_all_pwm(0, servo_min)
    time.sleep(2)
    pwm.set_all_pwm(0, servo_max)
    time.sleep(2)
    i = i + 1

#stop servos with pulse 350
pwm.set_all_pwm(0, servo_stop)