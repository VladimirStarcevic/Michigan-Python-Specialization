from typing import Dict, Tuple

def get_num_of_pokemons(dict_in: Dict) -> Tuple[int, int, int]:
     rattats = 0
     dittos = 0
     pidgeys = 0
     for trainer_data in dict_in.values():

         if isinstance(trainer_data, dict):
             for pokemon_data in trainer_data.values():
                 if isinstance(pokemon_data, dict):
                     rattats += pokemon_data.get("rattatas", 0)
                     dittos += pokemon_data.get("ditto", 0)
                     pidgeys += pokemon_data.get("pidgey", 0)
     return  rattats, dittos, pidgeys

pokemon = {'Trainer1':
                   {'normal':
                        {'rattatas': 15, 'eevees': 2, 'ditto': 1},
                    'water':
                        {'magikarps': 3},
                    'flying':
                        {'zubats': 8, 'pidgey': 12}},

           'Trainer2':
                   {'normal': {'rattatas': 25, 'eevees': 1},
                    'water': {'magikarps': 7},
                    'flying': {'zubats': 3, 'pidgey': 15}},

           'Trainer3':
                   {'normal': {'rattatas': 10, 'eevees': 3, 'ditto': 2},
                    'water': {'magikarps': 2},
                    'flying': {'zubats': 3, 'pidgey': 20}},
           'Trainer4':
                   {'normal': {'rattatas': 17, 'eevees': 1},
                    'water': {'magikarps': 9},
                    'flying': {'zubats': 12, 'pidgey': 14}}}


r, d, p = get_num_of_pokemons(pokemon)

print(f"Rattatas: {r}\nDittos: {d}\nPidgey: {p}")
