import unittest
import requests
import json

class TestpokemonIndex(unittest.TestCase):

    SITE_URL = 'http://localhost:51055' # replace with your assigned port id
    print("Testing for server: " + SITE_URL)
    POKEMON_URL = SITE_URL + '/pokemon/'
    RESET_URL = SITE_URL + '/reset/'

    def reset_data(self):
        m = {}
        r = requests.put(self.RESET_URL, json.dumps(m))

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_pokemon_index_get(self):
        self.reset_data()
        r = requests.get(self.POKEMON_URL)
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        testpokemon = {}
        for poke in resp['pokemon'][0]:
            if poke['name']['english'] == 'Charizard':
                testpokemon = poke

        self.assertEqual(testpokemon['name']['english'], 'Charizard')
        self.assertEqual(testpokemon['type'][0], 'Fire')

    def test_pokemon_index_post(self):
        self.reset_data()

        m = {}
        m['name'] = 'Yaseen'
        m['types'] = 'Water'
        m['image'] = 'hello'
        m['base'] = '???'
        r = requests.post(self.POKEMON_URL, data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['id'], 810)

        r = requests.get(self.POKEMON_URL + str(m['name']))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())

    #    print("here is error:" + resp['name'] + "and" + m['name'])
        print(" response is :" + str(resp))
        self.assertEqual(str(resp['name']), str(m['name']))
        self.assertEqual(resp['types'], m['types'])

    def test_pokemon_index_delete(self):
        self.reset_data()

        m = {}
        r = requests.delete(self.POKEMON_URL, data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        print(resp)
        self.assertTrue(resp['result'], 'success')

        r = requests.get(self.POKEMON_URL)
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        pokemon = resp['pokemon']
        self.assertTrue(pokemon, [[]])

if __name__ == "__main__":
    unittest.main()
