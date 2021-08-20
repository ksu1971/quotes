from flask import Flask ,render_template

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/tables')
def tables():
    return '<h1> Hello World from Tables</h1>'

@app.route('/seats')
def seats():
    return '<h1> Hello World from Seats</h1>'