import requests

URL = ' https://api.pokemonbattle.ru/v2'
TOKEN = 'dda8d670e03917130c0ac5f5cdc9fa06'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
body_create = {
    "name": "Жэээс1311",
    "photo_id": 12
}

response_created = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_created.json)

poke_id = response_created.json()['id']

body_change = {
    "pokemon_id": poke_id,
    "name": "New Name123"
}

name_change = requests.patch(url=f'{URL}/pokemons', headers=HEADER, json=body_change)
print(name_change.json())

catching_poke = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json={"pokemon_id": poke_id})
print(catching_poke.text)


''' Создание покемона (**POST /pokemons** (*не забудь про нужный хэдер*))'''
'''В ответе (терминале) должен прийти объект json'''
'''Смена имени покемона (**PUT /pokemons** (*не забудь про нужный хэдер*))'''
'''В ответе (терминале) должен прийти объект json'''
'''Поймать покемона в покебол (**POST /trainers/add_pokeball** (*не забудь про нужный хэдер*))'''
