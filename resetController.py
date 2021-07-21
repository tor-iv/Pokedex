import cherrypy
import re, json
from pokemon_library import _pokemon_database

class ResetController(object):

	def __init__(self, pdb=None):
		# if pdb is None:
		# 	self.pdb = _pokemon_database()
		# else:
		self.pdb = pdb

	def PUT_INDEX(self):
		output = {'result' : 'success'}
		data = json.loads(cherrypy.request.body.read().decode())
		# tmppdb = _pokemon_database()
		# tmppdb.load_pokemon('pokemon.json')
		# self.pdb = tmppdb
		self.pdb.reset_data()
		# self.pdb = _pokemon_database()
		# self.pdb.load_pokemon('pokemon.json')
		print("newly reset self.pdb.pokemon_data is: ********************** ")
		print("get pokemon after reset put index ")
		print(self.pdb.get_pokemon('bulbasaur'))
		# print(str(self.pdb.pokemon_data))
		#self.pdb.load_ratings('ratings.dat') replace with images or seperate type file?
		return json.dumps(output)

	def PUT_KEY(self, pokemon_name):
		output = {'result' : 'success'}
		pid = str(pokemon_name)
	
		try:
			data = json.loads(cherrypy.request.body.read().decode())

			pdbtmp = _pokemon_database()
			pdbtmp.load_pokemon('pokemon.json')
			# poke = self.pdb.pokemon_data
			# for i in range (0,(len(poke))):
			# 	if (pid.lower() == self.pdb[i]['name']['english'].lower()):
			pokemon = pdbtmp.get_pokemon(pid)
			print("pokemon at put_key is: " + str(pokemon))
			self.pdb.set_pokemon(pid, pokemon)

		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)
