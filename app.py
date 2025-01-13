from flask import Flask, render_template, request
from pokemon_service import PokemonService
import requests

app = Flask(__name__)
pokemon_service = PokemonService()

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/index')
def index():
    pokemon_types = pokemon_service.get_pokemon_types()
    return render_template('index.html', pokemon_types=pokemon_types)

@app.route('/pokemon', methods=['GET'])
def get_pokemon():
    pokemon_name = request.args.get('name')
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    if response.status_code == 200:
        pokemon_data = response.json()
        return render_template('pokemon.html', pokemon=pokemon_data)
    else:
        return "Pokémon not found", 404

@app.route('/type/<type_name>')
def get_pokemon_by_type(type_name):
    try:
        pokemon_list = pokemon_service.get_pokemon_by_type(type_name)
        return render_template(f'{type_name}.html', pokemon_list=pokemon_list)
    except Exception as e:
        return str(e), 500

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{query}')
    if response.status_code == 200:
        pokemon_data = response.json()
        return render_template('pokemon.html', pokemon=pokemon_data)
    else:
        return "Pokémon not found", 404

if __name__ == '__main__':
    app.run(debug=True)
