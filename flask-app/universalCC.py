import math
import time
from flask import Flask, render_template, Response
from turbo_flask import Turbo
import asyncio

app = Flask(__name__)
turbo = Turbo(app)


@app.route('/text')
def text():
    """
    Render the content a url different from index
    """
    def inner():
        # simulate a long process to watch
        for i in range(500):
            j = math.sqrt(i)
            time.sleep(1)
            # this value should be inserted into an HTML template
            yield str(i)
    return Response(inner(), mimetype='text/html')


@app.route("/")
def hello_world():
    return render_template('index.html.jinja')
