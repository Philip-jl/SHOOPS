from flask import Flask, render_template
import os

app = Flask(__name__)
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarning(False)
@app.route('/')

def hello():
    return render_template('index.html')

@app.route("/start/", methods=['POST'])
def run_script():
    file = open(r'total.py','r').read()
    exec(file)
    return render_template('index.html')

@app.route("/filter/", methods=['POST'])
def run_filter():
    file = open(r'RelayCon_SHOOPS.py','r').read()
    exec(file)
    return render_template('index.html')

@app.route("/stop/", methods=['POST'])
def run_stop():
    file = open(r'GPIO_cleanup.py','r').read()
    exec(file)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
