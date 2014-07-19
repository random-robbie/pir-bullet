pir-bullet
==========

Raspberry Pi PIR Intruder Alerts Via Push Bullet

This will take a photo with the raspberry pi cam and then send the photo to your mobile or mac or pc via pushbullet

Requirements
----

```
sudo apt-get update
sudo apt-get install python-setuptools python-picamera python-rpi.gpio -y
sudo easy_install pip
sudo pip install websocket-client requests python-magic
```

You will also need a pushbullet account from http://www.pushbullet.com

Config
---

You need to put your pushbullet API key in to pirmine.py

```
apiKey = "" and insert your pushbullet api key
```



Thanks to 
---

PyPushbullet - https://github.com/Azelphur/pyPushBullet

python-picamera-setup - https://github.com/raspberrypilearning/python-picamera-setup

