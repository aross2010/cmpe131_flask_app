from flask import render_template
from flask import flash
from flask import redirect
from app import app


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results')
def results(): 
    return render_template('results.html')

