import paho.mqtt.client as mqtt
import time
from grovepi import *
from grove_rgb_lcd import *

if __name__ == '__main__':
    client = mqtt.Client()
    client.connect(host="eclipse.usc.edu", port=1883, keepalive=60)
    client.loop_start()
    PORT = 3
    buzzer = 8
    pinMode(buzzer, "OUTPUT")
    count = 0
    buzzer_on = False
    digitalWrite(buzzer, 0)
    while True:
        digitalWrite(buzzer, 0)
        if buzzer_on:
            digitalWrite(buzzer, 1)
            continue # Delete later
        client.publish("bailey/ultrasonicRanger", ultrasonicRead(PORT))
        if ultrasonicRead(PORT) < 100:
            count += 1
            if count == 5:
                buzzer_on = True
                # Shoot gun
                count = 0
                continue # Delete later
        time.sleep(1)