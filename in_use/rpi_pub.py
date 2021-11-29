import paho.mqtt.client as mqtt
import time
from grovepi import *
from grove_rgb_lcd import *

if __name__ == '__main__':
    client = mqtt.Client()
    client.connect(host="eclipse.usc.edu", port=1883, keepalive=60)
    client.loop_start()
    PORT = 3
    while True:
        print(ultrasonicRead(PORT))
        client.publish("bailey/ultrasonicRanger", ultrasonicRead(PORT))
        time.sleep(1)