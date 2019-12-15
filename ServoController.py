#!/usr/bin/env python3

## Authors: Sean McAtee, Merai Dandouch
## Version: 12/10/2019

## About:
#       This program is for a Raspberry Pi connected to an Adafruit Driver to control the speed of 12 servo motors.
#       Pi: Raspberry Pi 3 Model B
#       Driver: Adafruit CA9685 16-Channel 12-Bit PWM Driver

# Dependencies:
#   RPi.GPIO
#       pip install RPi.GPIO


# Do we need to add a capacitor to our hat??
#when setting up use 'sudo i2cdetect -y 1' to find the pin address

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

#Using BOARD mode to reference pins because it is more stable if the Pi is changed
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Set output channels
chan_list = []

GPIO.setup(chan_list, GPIO.OUT)

#p = GPIO.PWM(channel, frequency)

#dc = duty cycle between 0.0 and 100.0
#p.start(dc)
#p.ChangeFrequency(frequency in Hz)
#p.ChangeDutyCycle(dc)
#p.stop()