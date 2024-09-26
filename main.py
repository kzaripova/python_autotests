import requests
import random
import string

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'bfac8cdb4ecf0619af5572b2c6421c26'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}

def generate_random_name(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

body_create_pokemon = {
    "name": generate_random_name(),
    "photo_id": -1
}

response_create = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_create_pokemon)
print(f"Status Code: {response_create.status_code}")
print("Response (JSON):", response_create.text)

pokemon_id = response_create.json().get("id")
print(f"Created Pokemon ID: {pokemon_id}")

body_change_pokemon = {
    "pokemon_id": pokemon_id,  
    "name": generate_random_name(),           
    "photo_id": -1
}

response_change = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_change_pokemon)
print(f"Status Code: {response_change.status_code}")
print("Response (JSON):", response_change.text)

body_add_pokeball = {
    "pokemon_id": pokemon_id  
}

response_add_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_add_pokeball)
print(f"Status Code: {response_add_pokeball.status_code}")
print("Response (JSON):", response_add_pokeball.text)