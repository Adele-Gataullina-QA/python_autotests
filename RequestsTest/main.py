import requests
import json

token = '31269a2ef0a606f864b20ec18a3d44cd'

response_creation = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token}, json={
    "name": "Шушун",
    "photo": "https://www.pngplay.com/wp-content/uploads/10/Pokemon-Transparent-Image.png"
})
print(response_creation.text)

id_of_pokemon = response_creation.json()['id']

response_update = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token}, json={
    "pokemon_id": f'{id_of_pokemon}',
    "photo": "https://freepngimg.com/thumb/pokemon/20346-7-pokemon-hd.png"
})
print(response_update.text)

response_pokebol = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers={'trainer_token': token}, json={
    "pokemon_id": f'{id_of_pokemon}'
})
print(response_pokebol.text)