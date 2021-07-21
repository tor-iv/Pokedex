import unittest
import requests
import json

class TestMovies(unittest.TestCase):

    SITE_URL = 'http://localhost:51055' # replace with your port number and 
    print("testing for server: " + SITE_URL)
    POKEMON_URL = SITE_URL + '/pokemon/'
    RESET_URL = SITE_URL + '/reset/'

    def reset_data(self):
        m = {}
        r = requests.put(self.RESET_URL, data = json.dumps(m))


    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_pokemon_get_key(self):
        self.reset_data()
        pokemon_id = 'Bulbasaur'
        r = requests.get(self.POKEMON_URL + str(pokemon_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['name'], 'Bulbasaur')
        self.assertEqual(resp['types'][0], 'Grass')

    def test_pokemon_put_key(self):
        self.reset_data()
        pokemon_id = 'Squirtle'

        r = requests.get(self.POKEMON_URL + str(pokemon_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        print("repsonse on line 56 is :" + str(resp))
        self.assertEqual(resp['name'], 'Squirtle')
        self.assertEqual(resp['types'][0], 'Water')

        m = {}
        m['name'] = 'Squirtle'
        m['types'] = 'Fire'
        m['image'] = 'hello'
        m['base'] = '???'
        r = requests.put(self.POKEMON_URL + str(pokemon_id), data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.POKEMON_URL + str(pokemon_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        
        self.assertEqual(str(resp['name']), str(m['name']))
        self.assertEqual(str(resp['types']), str(m['types']))

    def test_pokemons_delete_key(self):
        self.reset_data()
        pokemon_id = 'Venusaur'

        m = {}
        r = requests.delete(self.POKEMON_URL + str(pokemon_id), data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        print("repsonse of line 67 is: " + str(resp))
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.POKEMON_URL + str(pokemon_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'error')
        #self.assertEqual(resp['message'], 'movie not found')

if __name__ == "__main__":
    unittest.main()

