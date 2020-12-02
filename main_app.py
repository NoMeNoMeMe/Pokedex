from bs4 import BeautifulSoup
import requests
import csv


def get_pokemon_data(first_entry):

    poke_name = ''
    poke_number = 0

    try:
        with open("pokemon.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                if first_entry == '' or first_entry == '0':
                    print("You must enter something")
                    break
                # checks if string contains only digits
                elif first_entry.isdigit():
                    # makes number 3 digits with zeros at the beginning for searching in csv file
                    first_entry = first_entry.zfill(3)
                    search_num = first_entry
                    if search_num in row[0]:
                        poke_name = row[1]
                        poke_number = row[0]
                elif first_entry.lower() in str(row[1]).lower():
                    poke_name = row[1]
                    poke_number = row[0]
                else:
                    print("Pokemon not found")
                    break

        html = requests.get(f'https://bulbapedia.bulbagarden.net/wiki/{poke_name}_(Pok%C3%A9mon)').text
        soup = BeautifulSoup(html, 'lxml')
        container = soup.body.find('div', class_="mw-body")

        name = str(container.find('td', class_='roundy').find('b'))
        name_final = name.replace('<b>', '').replace('</b>', '')
        print(f'\nName: {name_final}\n')
        poke_number_print = poke_number.zfill(3)
        print(f'Pokedex number: {poke_number_print}\n')
        image = container.find('a', class_='image').img['src']
        image_full = f'https:{image}'
        print(f'Image link: {image_full}\n')
        poke_types = container.find('table', class_='roundy', attrs={'style':'background: #FFF; padding-top: 3px;'}).tr.td.table.tr
        poke_types = poke_types.find_all('td')

        type_num = 1
        unknown = 'Unknown'
        for i in poke_types:
            poke_type = str(i.find('a').b)
            poke_type = poke_type.replace('<b>', "").replace('</b>', '')
            if poke_type is not unknown:
                print(f'{poke_name}\'s type {type_num} is: {poke_type}\n')
                type_num += type_num
            elif poke_type == unknown:
                break

        pokemon_games_list= []
        pokemon_descriptions = []


        pokedex_entries_all = container.find('div', id='outercontentbox').find('div', id='contentbox').find('div', id='bodyContent').find('div', id='mw-content-text').find('table', class_='roundy', attrs={'style':'margin:auto; border: 3px solid #A040A0; background: #78C850; padding:2px; width: 100%; max-width: 740px;'})
        pokedex_entries_all_list = pokedex_entries_all.find_all('table', class_='roundy', attrs={'style':'background: transparent; border-collapse:collapse;'})
        for pokedex_entry in pokedex_entries_all_list:
            generation = pokedex_entry.tr.th.small.text
            games = pokedex_entry.find_all('th', class_='roundy')

            print(f'{generation}\n')

            # for game_name in games:
            #     game = game_name.a['title']
            #     if game not in pokemon_games_list[-1:]:
            #         pokemon_games_list.append(game)
            #         # print(f'Appending: {game}')
            #
            #     print(f'Game: {game}')

            all_texts = pokedex_entry.find_all('td', class_='roundy')
            # print(f'Find all texts {all_texts}')
            for text in all_texts:
                poke_description = text.text
                if poke_description not in pokemon_descriptions[-1:]:
                    pokemon_descriptions.append(poke_description)
                    # print(f'Appending: {poke_description}')
                print(f'{poke_description}')


    except AttributeError:
        # HTML parsing not working for every site
        print("Work in progress")






        # print(games)

        # print(f'Pokedex entry {pokedex_entry}')
        # print('*******************************************')

    # i = 0
    # j = 0
    # print(len(pokemon_games_list))
    # print(len(pokemon_descriptions))


    # for numb in pokemon_games_list:
    #     print(pokemon_games_list[i])
    #     print(pokemon_descriptions[i])
    #     i += 1
    # for numb in pokemon_descriptions:
    #     print(pokemon_descriptions[j])
    #     j += 1

    # print(pokemon_games_list)
    # print(pokemon_descriptions)
    return poke_name, poke_number, image_full, poke_type, pokemon_games_list, pokemon_descriptions


# Last time checked working (kind of) at 19.11.2020
