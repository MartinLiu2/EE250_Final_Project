import paho.mqtt.client as mqtt
import time
from grovepi import *
from grove_rgb_lcd import *

if __name__ == '__main__':
    client = mqtt.Client()
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()
    PORT = 3
    button = 8
    pinMode(button, "INPUT")
    while True:
        client.publish("bailey/ultrasonicRanger", ultrasonicRead(PORT))
        time.sleep(1)