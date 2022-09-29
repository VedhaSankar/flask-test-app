from flask import Flask, render_template
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

PORT = os.environ.get('PORT')

app = Flask(__name__)

@app.route('/')
def start():

    return render_template('index.html')

@app.route('/ping')
def ping():

    result = {
        "ping"  : "pong"
    }
    return result

@app.route('/time')
def time():
    
    result = {
        "current_time"  : datetime.datetime.now().strftime("%H:%M:%S"),
        "current_date"  : datetime.datetime.now().strftime("%Y-%m-%d")
    }

    return result

if __name__== "__main__":
    app.run(host="0.0.0.0", debug = True, port = 5003)