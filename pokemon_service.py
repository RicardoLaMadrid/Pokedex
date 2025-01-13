import requests

class PokemonService:
    base_url = 'https://pokeapi.co/api/v2'

    def get_pokemon_types(self):
        response = requests.get(f'{self.base_url}/type')
        if response.status_code == 200:
            return response.json()['results']
        else:
            raise Exception('Failed to load Pokémon types')

    def get_pokemon_by_type(self, type_name):
        response = requests.get(f'{self.base_url}/type/{type_name}')
        if response.status_code == 200:
            pokemon_list = response.json()['pokemon']
            detailed_pokemon_list = []
            for pokemon in pokemon_list:
                pokemon_data = self.get_pokemon(pokemon['pokemon']['url'])
                detailed_pokemon_list.append(pokemon_data)
            return detailed_pokemon_list
        else:
            raise Exception(f'Failed to load Pokémon of type {type_name}')

    def get_pokemon(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Failed to load Pokémon data')


