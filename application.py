from flask import Flask, render_template
import totals


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/totales')
def get_totals():
    results = totals.compute_from('pauta-oficial-primer-semestre-2016.csv')
    advertisers, campaigns, media, total = results
    
    return 'This should return totals computed from a CVS file.'
