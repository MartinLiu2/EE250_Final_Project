from flask import Flask, request, render_template
from flask_mqtt import Mqtt


app = Flask(__name__)
intruder_status = 0
threshold_value = 50
alarm_count = 0
intruder_detected = False

app.config['MQTT_BROKER_URL'] = 'eclipse.usc.edu'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_KEEPALIVE'] = 60

mqtt = Mqtt(app)

@mqtt.on_topic('bailey/ultrasonicRanger')
def ultrasonic_callback(client, userdata, msg):
    global intruder_status, alarm_count, intruder_detected
    intruder_status = msg.payload.decode("utf-8", "strict")
    if int(intruder_status) <= threshold_value:
        alarm_count += 1
        print(alarm_count)
        if alarm_count == 5:
            intruder_detected = True
            print(intruder_detected)

    # Take output and give it to website.py to determine if door close/open

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    client.subscribe('bailey/ultrasonicRanger')
    client.message_callback_add('bailey/ultrasonicRanger', ultrasonic_callback)


@mqtt.on_message()
def once_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

@app.route('/')
def index():
    global intruder_detected, alarm_count
    intruder_detected = False
    alarm_count = 0
    return render_template('website_disarmed.html')

@app.route('/alarm_armed')
def alarm_armed():
    return render_template('website_armed.html', Intruder=intruder_detected)

if __name__ == "__main__":
    app.run(debug=True)