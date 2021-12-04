import paho.mqtt.client as mqtt
import time
from gpiozero import AngularServo

#servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)
motorOn = False
flag = 0
def shoot_callback(client, userdata, msg):
    output = msg.payload.decode("utf-8", "strict")
    # Take output and give it to website.py to determine if shoot
    print(type(output))
    global motorOn
    motorOn = True
    #servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)
    #servo.angle = 90

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to the shoot topic here
    client.subscribe("bailey/shoot")
    client.message_callback_add("bailey/shoot", shoot_callback)

def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

if __name__ == '__main__':
        #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=1883, keepalive=60)
    client.loop_start()

    while True:
        time.sleep(1)
        if motorOn:
           flag += 1
           if flag == 1:
	      servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)
              flag += 1
           servo.angle = 90 
