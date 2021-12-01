import paho.mqtt.client as mqtt
import time
from grovepi import *
from grove_rgb_lcd import *

if __name__ == '__main__':
    client = mqtt.Client()
    client.connect(host="eclipse.usc.edu", port=1883, keepalive=60)
    client.loop_start()
    PORT = 3
    count = 0
    buzzer_on = False
    while True:
        if buzzer_on:
            # Ring buzzer
            continue # Delete later
        client.publish("bailey/ultrasonicRanger", ultrasonicRead(PORT))
        if ultrasonicRead(PORT) < 50:
            count += 1
            if count == 5:
                buzzer_on = True
                # Ring buzzer
                # Shoot gun
                count = 0
                continue # Delete later
        time.sleep(1)