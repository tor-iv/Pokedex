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


       def load_ratings(self, ratings_file):
        f = open(ratings_file)
        for line in f:
                line = line.rstrip()
                components = line.split("::")
                uid = int(components[0])
                mid = int(components[1])
                rating = int(components[2])
                self.pokemon_ratings[mid][uid] = rating
        f.close()

       def get_rating(self, mid):
        avg = 0
        total = 0
        mratings = self.pokemon_ratings[mid]
        for rating in mratings.values():import json
class _pokemon_database:

       def __init__(self):
        self.pokemon_data = dict()

       def load_pokemon(self, pokemon_file):
        f = open(pokemon_file)
        data = json.load(f)
        self.pokemon_data = data
        f.close()

       def get_pokemon(self):
        return self.pokemon_names.keys()

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

       #### pokemon ########
       mdb.load_pokemon('pokemon.dat')

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


                avg += rating
                total += 1
        if total == 0:
                total = 1
        return (avg / float(total))

       def get_highest_rated_unvoted_pokemon(self, user_id):
           highest_user_rating = 0
           highest_rated_mid = 0
           for cur_mid in self.pokemon_names.keys():
             if cur_mid in self.pokemon_ratings and user_id in self.pokemon_ratings[cur_mid]:
               continue
             cur_avg_rating = self.get_rating(cur_mid)
             if (cur_avg_rating > highest_user_rating):
                highest_user_rating = cur_avg_rating
                highest_rated_mid = cur_mid
           return(highest_rated_mid)

       def get_highest_rated_pokemon(self):
        highest_user_rating = 0
        highest_rated_mid = 0
        for cur_mid in self.pokemon_names.keys():
                cur_avg_rating = self.get_rating(cur_mid)
                if (cur_avg_rating > highest_user_rating):
                        highest_user_rating = cur_avg_rating
                        highest_rated_mid = cur_mid
        return(highest_rated_mid)


       def delete_all_ratings(self):
        for mid in self.get_pokemons():
                self.pokemon_ratings[mid] = dict()

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

