import main_app as pokedex

num = 0
max_num = 750

for num in range(0, 750):
    pokedex.get_pokemon_data(num)
    num += 1

