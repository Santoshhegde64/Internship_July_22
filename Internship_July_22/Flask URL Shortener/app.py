from flask import Flask
from flask import render_template
from flask import request
import pyshorteners
from flask import redirect
from flask import url_for

app = Flask(__name__)


@app.route("/", methods = ['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route("/convert", methods = ['GET'])
def short_function():
    url = request.args['url_name']
    s = pyshorteners.Shortener() # Pyshortener object
    short_url = s.tinyurl.short(url)
    short_url = str(short_url)
    return "The Shortened URL is:{}".format(short_url)

if __name__ == "__main__":
    app.run(debug = True)