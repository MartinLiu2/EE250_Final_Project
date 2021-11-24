from flask import Flask, request, render_template

app = Flask(__name__)
intruder_status = True

@app.route('/')
def index():
    return render_template('website_disarmed.html')

@app.route('/alarm_armed')
def alarm_armed():
    return render_template('website_armed.html', Intruder=intruder_status)

if __name__ == "__main__":
    app.run(debug=True)