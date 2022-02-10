from flask import Flask, render_template

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


if __name__== "__main__":
    app.run(host="0.0.0.0", debug = True, port = 5003)