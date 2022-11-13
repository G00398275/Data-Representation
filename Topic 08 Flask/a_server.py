# Data Representation - Winter 2022
# Flask Application Server
# Author: Ross Downey
# Lecturer: Andrew Beatty

from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "Hello World Again"

if __name__ == "__main__":
    app.run(debug = True)