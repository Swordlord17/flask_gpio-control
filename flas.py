import RPi.GPIO as G
import time

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "flask server up!"

@app.route("/servo")
def servo():
    servoPIN = 17
    G.setmode(G.BCM)
    G.setup(servoPIN, G.OUT)
    p = G.PWM(servoPIN, 50)
    p.start(2.5)
    try:
        while True:
            p.ChangeDutyCycle(5)
            time.sleep(0.5)
            p.ChangeDutyCycle(7.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(10)
            time.sleep(0.5)
            p.ChangeDutyCycle(12.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(10)
            time.sleep(0.5)
            p.ChangeDutyCycle(7.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(5)
            time.sleep(0.5)
            p.ChangeDutyCycle(2.5)
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        
            p.stop()
            G.cleanup()

app.run(debug=True, host='0.0.0.0')
            

            
     

    
