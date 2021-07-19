import unittest
import requests
import json

class TestReset(unittest.TestCase):

	SITE_URL = 'http://localhost:51055'
	print('Testing for server: ' + SITE_URL)
	RESET_URL = SITE_URL + '/reset/'

	def test_put_reset_index(self):
		m = {}
		r = requests.put(self.RESET_URL, json.dumps(m))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')
		r = requests.get(self.SITE_URL + '/pokemon/')
		resp = json.loads(r.content.decode())
		pokemon = resp['pokemon']
		self.assertEqual(pokemon[0]['name'], 'Bulbasaur')

	def test_put_reset_key(self):
		m = {}
		r = requests.put(self.RESET_URL, json.dumps(m))

		# Change Movie Title and Genre
		pokemon_id = 'Bulbasaur'
		m['name'] = 'Shreya'
		m['type'] = 'Fire'
		r = requests.put(self.SITE_URL + '/pokemon/' + str(pokemon_id), data=json.dumps(m))

		# Reset the changed movie back to original
		m = {}
		r = requests.put(self.RESET_URL + str(pokemon_id), data=json.dumps(m))
		resp = json.loads(r.content.decode())	
		self.assertEqual(resp['result'], 'success')

		# Check if effective
		r = requests.get(self.SITE_URL + '/pokemon/')
		resp = json.loads(r.content.decode())	
		pokemon = resp['pokemon']
		self.assertEqual(pokemon[0]['name']['english'], 'Bulbasaur')




if __name__ == '__main__':
		unittest.main()





