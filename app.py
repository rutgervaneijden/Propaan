import flask
import requests

def get_facts():
    return requests.get('https://bestat.statbel.fgov.be/bestat/api/views/ef2a5bfb-a361-47a6-b113-e3df26563404/result/JSON').json()['facts']

app = flask.Flask(__name__)

@app.route('/')
def index():
    labels = list()
    data = list()
    facts = get_facts()
    for fact in facts:
        if fact['Product'] == 'propaan (in bulk) (minder dan 2000 l) (€/L)':
            labels.append(fact['Dag'])
            data.append(fact['Prijs incl. BTW'])
    return flask.render_template('index.html', labels=labels, data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)