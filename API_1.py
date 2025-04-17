import requests

base_url = "https://pokeapi.co/api/v2/"

def pokemon(name):
    url =f"{base_url}pokemon/{name.lower()}"
    response = requests.get(url)
    if response.status_code ==200:
        data = response.json()
        return data
    else:
        print("Error retrieving data")


pokemon_name = input("Enter the name of the Pokemon: ")
pokemon_info = pokemon(pokemon_name)

if pokemon_info:
    print(f"Nmae: {pokemon_info['name'].capitalize()}")
    print(f"Height: {pokemon_info['height']}")  
    print(f"Weight: {pokemon_info['weight']}")
    print(f"ID: {pokemon_info['id']}") 