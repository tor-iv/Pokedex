import json
class _pokemon_database:

       def __init__(self):
        self.pokemon_data =  dict()
        self.pokemon_names = list()
        self.pokemon_types = list()

       def load_pokemon(self, pokemon_file):
        # load data
        f = open('pokemon.json')
        data = json.load(f)
        self.pokemon_data = data
        f.close()
        #load names and types
        for i in data:
                name = i['name']['english']
                self.pokemon_name.append(name)
                types = i['types']
                self.pokemon_types.append(types)
        

       def get_pokemon(self):
               return self.pokemon_names

       def get_pokemon(self, mid):
        
        try:
                mname = self.pokemon_names[mid]
                mgenres = self.pokemon_genres[mid]
                pokemon = list((mname, mgenres))
        except Exception as ex:
                pokemon = None
        return pokemon

       def set_pokemon(self, mid, pokemon):
        self.pokemon_names[mid] = pokemon[0]
        self.pokemon_genres[mid] = pokemon[1]

        if mid not in self.pokemon_ratings.keys():
                self.pokemon_ratings[mid] = dict()

       def delete_pokemon(self, mid):
        del(self.pokemon_names[mid])
        del(self.pokemon_genres[mid])
        del(self.pokemon_ratings[mid])

if __name__ == "__main__":
       mdb = _pokemon_database()

       #### pokemonS ########
       mdb.load_pokemons('pokemons.dat')

       pokemon = mdb.get_pokemon(2)
       print(pokemon[0])

       pokemon[0] = 'ABC'
       mdb.set_pokemon(2, pokemon)

       print("A")
       print(mdb.get_rating(51))
       print("B")

       pokemon = mdb.get_pokemon(2)
       print(pokemon[0])
       ####################

       #### RATINGS #######
       mdb.load_ratings('ratings.dat')

       rating = mdb.get_rating(1)
       print(rating)

       hrm_mid = mdb.get_highest_rated_pokemon()
       hrm_rating = mdb.get_rating(hrm_mid)
       hrm = mdb.get_pokemon(hrm_mid)
       hrm_name = hrm[0]
       print(hrm_mid, hrm_name, hrm_rating)
       ####################

