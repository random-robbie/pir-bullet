#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import picamera
import datetime
from pushbullet import PushBullet
import os

apiKey = ""
p = PushBullet(apiKey)
devices = p.getDevices()

def removeoldpics():
	 os.remove(fileName)

def getFileName():
	return datetime.datetime.now().strftime ("%Y-%m-%d_%H.%M.%S.jpg")


	
sensorPin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

prevState = False
currState = False

cam = picamera.PiCamera()

while True:
	time.sleep(.1)
	prevState = currState
	currState = GPIO.input(sensorPin)
	if currState != prevState:
		print "GPIO pin {0} is {1}".format(sensorPin, "HIGH" if currState else "LOW")
		if currState:
			fileName = getFileName()
			cam.start_preview()
			cam.capture(fileName)
			p.pushFile(devices[0]["iden"], "Intruder Alert!", open(fileName, "rb"))
			cam.stop_preview()
			time.sleep(5)
			removeoldpics()
		else:
			cam.stop_preview()
			
			
