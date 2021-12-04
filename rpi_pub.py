import paho.mqtt.client as mqtt
import time
from grovepi import *
from grove_rgb_lcd import *

armed = False 

def armed_callback(client, userdata, msg):
    output = msg.payload.decode("utf-8", "strict")
    # Take output and give it to website.py to determine if door close/open
    global armed
    armed = True
    print("Hello " + str(armed))

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to the ultrasonic ranger topic here
    client.subscribe("bailey/armed")
    client.message_callback_add("bailey/armed", armed_callback)

def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

if __name__ == '__main__':
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=1883, keepalive=60)
    client.loop_start()
    PORT = 3
    buzzer = 8
    pinMode(buzzer, "OUTPUT")
    count = 0
    armed = False
    buzzer_on = False
    digitalWrite(buzzer, 0)
    while True:
        digitalWrite(buzzer, 0)
        if buzzer_on:
            digitalWrite(buzzer, 1)
        client.publish("bailey/ultrasonicRanger", ultrasonicRead(PORT))
        print(ultrasonicRead(PORT))
        if not armed:
            continue
        if ultrasonicRead(PORT) < 100:
            count += 1
            if count == 5 and armed:
                buzzer_on = True
                client.publish("bailey/shoot", 1)
                count = 0
        time.sleep(0.2)
