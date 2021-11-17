import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
import json

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

iot_hub = "demo.thingsboard.io"
port = 1883
username = "2r4SGTFvaYPXyLGg2Nc8"
password =""
topic = "v1/devices/me/telemetry"

client = mqtt.Client()
client.username_pw_set(username,password)
client.connect(iot_hub,port)
print("Connection Successful")

data = dict()
while True:
    GPIO.output(18,GPIO.HIGH)
    print("FAN IS OFF")
    data["FAN-Status"] = "OFF"
    data_out = json.dumps(data)
    client.publish(topic,data_out,0)
    time.sleep(3)
    
    GPIO.output(18,GPIO.LOW)
    print("FAN IS ON")
    data["FAN-Status"] = "ON"
    data_out = json.dumps(data)
    client.publish(topic,data_out,0)
    time.sleep(3)
