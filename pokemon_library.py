import json
class _pokemon_database:
    def __init__(self):
        self.pokemon_data =  dict()
        self.pokemon_names = set()

    def load_pokemon(self, pokemon_file):
        # load data
        pokemon_file = str(pokemon_file)
        f = open(pokemon_file) #encoding = "utf8"
        data = json.load(f)
        self.pokemon_data = data
        for i in range (0,(len(self.pokemon_data))):
            if i+1 < 10:
                self.pokemon_data[i]['image'] = str("https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/00" + str(i+1) + ".png")
            elif (i+1) < 100:
                self.pokemon_data[i]['image'] = "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/0" + str(i+1) + ".png"
            else:
                self.pokemon_data[i]['image'] = "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/" + str(i+1) + ".png"
        f.close()
        #load names and type
        # for i in data:
        #     name = i['name']['english']
        #     self.pokemon_name.append(name)
        #     types = i['type']
        #     self.pokemon_type.append(types)
        
    def clear_data(self):
        self.pokemon_data = list()
        self.pokemon_names = set()
        
    def reset_data(self):
        self.clear_data()
        self.load_pokemon('pokemon.json')


    def get_pokemon_index(self):
        return self.pokemon_data

    def get_pokemon(self, pID):
        pID = str(pID)
        pokemon = []
        try:
            for i in range (0,(len(self.pokemon_data))):
                # print(len(self.pokemon_data)-1)
                # print(self.pokemon_data[-1])
                if (pID.lower() == self.pokemon_data[i]['name']['english'].lower()):
                    name = self.pokemon_data[i]['name']['english']
                    types = self.pokemon_data[i]['type']
                    stats = self.pokemon_data[i]['base']
                    image = self.pokemon_data[i]['image']
                    print(i)
                    # if i+1 < 10:
                    #     image = str("https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/00" + str(i+1) + ".png")
                    # elif (i+1) < 100:
                    #     image = "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/0" + str(i+1) + ".png"
                    # else:
                    #     image = "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/" + str(i+1) + ".png"
                    pokemon = list((name, types, stats, image))
                    break
        except IndexError:
            pokemon = None
        except Exception as ex:
            pokemon = None
        return pokemon

    def set_pokemon(self, name, pokemon):
        for i in range (0,len(self.pokemon_data)):
            if (self.pokemon_data[i]['name']['english'].lower() == name.lower()):
                self.pokemon_data[i]['name']['english'] = pokemon[0]
                self.pokemon_data[i]['type'] = pokemon[1]
                if pokemon[2]:
                    self.pokemon_data[i]['base'] = pokemon[2]
                if pokemon[3]:
                    self.pokemon_data[i]['image'] = pokemon[3]


    def delete_pokemon(self, name):
        for i in range (0,len(self.pokemon_data)-1):
            if (self.pokemon_data[i]['name']['english'].lower() == name.lower()):
                del(self.pokemon_data[i])

    def delete_all_pokemon(self):
        for i in range (0,len(self.pokemon_data)):
            del(self.pokemon_data[i])


if __name__ == "__main__":
    pdb = _pokemon_database()
    #### pokemon ########
    pdb.load_pokemon('pokemon.json')
    pokemon = pdb.get_pokemon('Bulbasaur')
    print(pokemon[0])
    pokemon[0] = 'ABC'
    mdb.set_pokemon('Bulbsaur', pokemon)
    print("A")
    print("B")
    pokemon = pdb.get_pokemon('Bulbasaur')
    print(pokemon[0])
       ####################
