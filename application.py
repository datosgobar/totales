from flask import Flask, render_template
import totals


app = Flask(__name__)

@app.route('/')
def index():    
    return render_template('index.html', totals=get_totals())


def get_totals():
    results = totals.compute_from('pauta-oficial-primer-semestre-2016.csv')
    advertisers, campaigns, media, total = results

    return {
        'advertisers': advertisers,
        'campaigns': campaigns,
        'media': media,
        'total': total
    }
