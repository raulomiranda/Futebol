from flask import Flask, jsonify, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Habilitar CORS para as rotas

api_key = '76d8a275032971dfc751fea6efeba504'
base_url = 'https://v3.football.api-sports.io'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transfers')
def transfers():
    endpoint = f'{base_url}/transfers'
    params = {
        'team': '131'
    }
    headers = {
        'x-rapidapi-host': 'v3.football.api-sports.io',
        'x-rapidapi-key': api_key
    }

    response = requests.get(endpoint, headers=headers, params=params)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run()