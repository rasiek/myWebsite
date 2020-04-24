from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projets')
def projets():
    return render_template('projets.html')

@app.route('/apropos')
def apropos():
    return render_template('apropos.html')
