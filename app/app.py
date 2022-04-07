from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from joblib import load
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html')
    else:
        mytype = request.form['selectype']
        if mytype=='Box':
            return render_template('index_hand.html')
        elif mytype=='DragandDrop':
            return render_template('html_drag.html')
        elif mytype=='Sound':
            return render_template('html_sound.html')
        else:
            return render_template('index.html')
