from flask_bootstrap import Bootstrap
from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

bootstrap = Bootstrap(app)


@app.route('/')
def hello_world():
    feeds = [
        {
            "id": "open_home_feed",
            "label": "Home Feed"
        }, {
            "id": "hashtags",
            "label": "Hashtags"
        }, {
            "id": "location",
            "label": "Locations"
        }
    ]

    return render_template('app.html', feeds=feeds)


@app.route('/json/script.json')
def getdata():
    with open('json/script.json') as f:
        d = json.load(f)
    return jsonify(d)


if __name__ == '__main__':
    app.run(debug=True)
