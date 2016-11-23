from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the homepage.'

@app.route('/totales')
def totals():
    return 'This should return totals computed from a CVS file.'

