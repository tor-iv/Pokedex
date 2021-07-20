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
        self.reset_data()t
        r = requests.get(self.POKEMON_URL)
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())

        testpokemon = {}
        pokemon = resp['pokemon']
        for pokemon in pokemon:
            if pokemon['name']['english'] == 'Charizard':
                testpokemon = pokemon

        self.assertEqual(testpokemon['name'], 'Charizard')
        self.assertEqual(testpokemon['type'][0], 'Fire')

    def test_pokemon_index_post(self):
        self.reset_data()

        m = {}
        m['name'] = 'Yaseen'
        m['type'] = 'Water'
        r = requests.post(self.POKEMON_URL, data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['id'], 810)

        r = requests.get(self.POKEMON_URL + str(resp['name']))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['name'], m['name'])
        self.assertEqual(resp['type'], m['type'])

    def test_pokemon_index_delete(self):
        self.reset_data()

        m = {}
        r = requests.delete(self.POKEMON_URL, data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.POKEMON_URL)
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        pokemon = resp['pokemon']
        self.assertFalse(pokemon)

if __name__ == "__main__":
    unittest.main()

