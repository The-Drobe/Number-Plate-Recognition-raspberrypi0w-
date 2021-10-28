#imports
from ntpath import join
from flask import Flask, request, render_template
import os
from flask import send_from_directory
app = Flask(__name__)
from threading import Thread
#import Detector
import Car_detection
import time
from multiprocessing import Process, process

car = Car_detection.Car()
#detector = Detector.detector()
image = "N/A"
@app.route('/')
def index():
    with open('licence.txt') as f:
        licence = f.readlines()
    
    items = []
    for i in range(len(licence)):
        an_item = dict(licence=licence[i], image = image)
        items.append(an_item)
    return render_template('index.html',items=items)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
        'favicon.ico',mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    #app.run(debug=True)
#Preparing parameters for flask to be given in the thread
#so that it doesn't collide with main thread
    kwargs = {'host': '0.0.0.0', 'port': 5000, 'threaded': True, 'use_reloader': False, 'debug': False}
#running flask thread
    flaskThread = Thread(target=app.run, daemon=True, kwargs=kwargs).start()
    flaskThread = Thread(target=car.Car()).start()
    #app.run()
    #app.run(debug=True)
    