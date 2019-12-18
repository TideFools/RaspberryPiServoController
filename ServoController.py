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


# Moves all servos through functional range of pulse lengths
print("Moving all servos through functional range")
i = servo_min
while i <= servo_max:
   pwm.set_all_pwm(0, i)
   time.sleep(0.05)
   i = i + 1
pwm.set_all_pwm(0, 0)

# Check movement of each servo
print("Check movement of each servo")
i = 0
while i <= 15:
    pwm.set_pwm(i, 0, servo_max)
    time.sleep(0.5)
    pwm.set_pwm(i, 0, 0)
    i = i + 1
pwm.set_all_pwm(0, 0)

# Moves each servo at different speeds
print("Move each servo at different speeds")
mod = servo_max - servo_min
i = 0
while i <= 5:
    pwm.set_pwm(1, 0, servo_min + ((i * 32) % mod))
    pwm.set_pwm(2, 0, servo_min + ((i * 15) % mod))
    pwm.set_pwm(3, 0, servo_min + ((i * 39) % mod))
    pwm.set_pwm(4, 0, servo_min + ((i * 27) % mod))
    pwm.set_pwm(5, 0, servo_min + ((i * 13) % mod))
    pwm.set_pwm(6, 0, servo_min + ((i * 14) % mod))
    pwm.set_pwm(7, 0, servo_min + ((i * 33) % mod))
    pwm.set_pwm(8, 0, servo_min + ((i * 24) % mod))
    pwm.set_pwm(9, 0, servo_min + ((i * 32) % mod))
    pwm.set_pwm(10, 0, servo_min + ((i * 87) % mod))
    pwm.set_pwm(11, 0, servo_min + ((i * 11) % mod))
    pwm.set_pwm(12, 0, servo_min + ((i * 17) % mod))
    pwm.set_pwm(13, 0, servo_min + ((i * 15) % mod))
    pwm.set_pwm(14, 0, servo_min + ((i * 19) % mod))
    pwm.set_pwm(15, 0, servo_min + ((i * 22) % mod))
    time.sleep(0.5)
    i = i + 1
pwm.set_all_pwm(0, 0)

# Start stop cycle at increasing rate
print("Start stop cycle at increasing rate")
i = 0.5
while i > 0.0:
    print (i)
    pwm.set_all_pwm(0, servo_max)
    time.sleep(i)
    pwm.set_all_pwm(0, 0)
    time.sleep(i)
    i = i - 0.01
pwm.set_all_pwm(0, 0)

# Warm up clockwise
print("Warm up clockwise")
i = 350
while i >= servo_min:
    pwm.set_all_pwm(0, i)
    time.sleep(0.25)
    i = i - 1
pwm.set_all_pwm(0, 0)

# Warm up counterclockwise
print("Warm up counterclockwise")
i = 354
while i <= servo_max:
    pwm.set_all_pwm(0, i)
    time.sleep(0.25)
    i = i + 1
pwm.set_all_pwm(0, 0)

#stop servos with pulse 350
pwm.set_all_pwm(0, 0)