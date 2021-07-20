import json
class _pokemon_database:
    def __init__(self):
        self.pokemon_data =  dict()
    def load_pokemon(self):
        # load data
        f = open('pokemon.json')
        data = json.load(f)
        self.pokemon_data = data
        f.close()
        #load names and type
        # for i in data:
        #     name = i['name']['english']
        #     self.pokemon_name.append(name)
        #     types = i['type']
        #     self.pokemon_type.append(types)
    
    def get_pokemon(self):
        return self.pokemon_data

    def get_pokemon(self, pID):
        pID = str(pID)
        try:
            for i in self.pokemon_data:
                if lower(pID) == lower(i['name']['english']):
                    name = self.pokemon_data[i]['name']['english']
                    types = self.pokemon_data[i]['type']
                    stats = self.pokemon_data[i]['base']
                    pokemon = list((name, types, stats))
        except Exception as ex:
            pokemon = None
        return pokemon

    def set_pokemon(self, name, pokemon):
        for i in self.pokemon_data:
            if lower(i['name']['english']) == lower(name):
                self.pokemon_data[i]['name']['english'] = pokemon[0]
                self.pokemon_data[i]['type'] = pokemon[1]
                self.pokemon_data[i]['image'] = pokemon[2]


    def delete_pokemon(self, name):
        for i in self.pokemon_data:
            if lower(i['names']['english']) == lower(name):
                del(self.pokemon_data[i])

if __name__ == "__main__":
    pdb = _pokemon_database()
    #### pokemon ########
    pdb.load_pokemons('pokemon.json')
    pokemon = pdb.get_pokemon('Bulbasaur')
    print(pokemon[0])
    pokemon[0] = 'ABC'
    mdb.set_pokemon('Bulbsaur', pokemon)
    print("A")
    print("B")
    pokemon = pdb.get_pokemon('Bulbasaur')
    print(pokemon[0])
       ####################

