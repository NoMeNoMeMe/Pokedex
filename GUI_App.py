import tkinter as tk
from main_app import get_pokemon_data as pokedex

window = tk.Tk()

window.title('PokeDex App (alpha version)')

window.geometry('1000x700')

welcome = tk.Label(window, text='Welcome to PokeDex app')

welcome.grid(column=0, row=0)

# def open_in_browser():
#     pass
#
#
# open_browser_button = tk.Button(window, text='Open in browser')
#
# open_browser_button.grid(column=1, row=0)

txt = tk.Entry(window, width=10)

txt.grid(column=0, row=6)

txt.focus()

def search():
    pok = txt.get()
    global poke_name, poke_number, image_full, poke_type, pokemon_games_list, pokemon_descriptions = pokedex(pok)


search_button = tk.Button(window, text='Search', command=search)

search_button.grid(column=0, row=8)


show_name = tk.Label(window, text=poke_name)

show_number = tk.Label(window, text=poke_number)

show_image = tk.Label(window, text=image_full)

show_type = tk.Label(window, text=poke_type)

show_games_list = tk.Label(window, text=pokemon_games_list)

show_descriptions = tk.Label(window, text=pokemon_descriptions)

show_name.grid(column=0, row=9)

show_number.grid(column=0, row=10)

show_image.grid(column=0, row=11)

show_type.grid(column=0, row=12)

show_games_list.grid(column=0, row=13)

show_descriptions.grid(column=0, row=14)

window.mainloop()
