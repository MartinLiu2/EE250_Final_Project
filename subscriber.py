import paho.mqtt.client as mqtt
import time

def ultrasonic_callback(client, userdata, msg):
    output = msg.payload.decode("utf-8", "strict")
    print("VM: " + output + " cm")

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to the ultrasonic ranger topic here
    client.subscribe("bailey/ultrasonicRanger")
    client.message_callback_add("bailey/ultrasonicRanger", ultrasonic_callback)

def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

if __name__ == '__main__':
        #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()

    while True:
        time.sleep(1)
