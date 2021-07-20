import cherrypy
import re, json
from pokemon_library import _pokemon_database

class PokemonController(object):

	def __init__(self, pdb=None):
		if pdb is None:
			self.pdb = _pokemon_database()
		else:
			self.pdb = pdb

		self.pdb.load_pokemon('pokemon.json') # was movies.dat


	def GET_KEY(self, pokemon_name):
		output = {'result' : 'success'}
		pokemon_name = str(pokemon_name)
		pokemon = []
		try:
			pokemon = self.pdb.get_pokemon(pokemon_name)
			if pokemon is not None:
				output['name'] = pokemon[0]
				output['types'] = pokemon[1]
				output['stats'] = pokemon[2]
				output['image'] = pokemon[3]
			#	output['title'] = movie[0] figure this out with JSON formatted file
			#	output['genres'] = movie[1]

			else:
				output ['result'] = 'error'
				output['message'] = 'pokemon not found'

		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex) + "messed up here"

		return json.dumps(output)

	def PUT_KEY(self, pokemon_name):
		output = {'result' : 'success'}
		pokemon_name = str(pokemon_name)

		data = json.loads(cherrypy.request.body.read().decode('utf-8'))

		pokemon = list()
		pokemon.append(data['name'])
		pokemon.append(data['types'])
		pokemon.append(data['base'])
		pokemon.append(data['image'])
		self.pdb.set_pokemon(pokemon_name, pokemon)

		return json.dumps(output)

	def DELETE_KEY(self, pokemon_id):
		
		output = {'result' : 'success'}

		pokemon_name = str(pokemon_name)

		try:
			self.pdb.delete_pokemon(pokemon_name)
		except Exception as ex:
			output['result'] = 'failure'
			output['message'] = str(ex)

		return json.dumps(output)

	def GET_INDEX(self):
		output = {'result' : 'success'}
		output['pokemon'] = []

		try:
			output['pokemon'].append(self.pdb.get_pokemon_index())
			# for pid in range(0, len(self.pdb.pokemon_data)):
			# 	output['pokemon'].append(self.pdb.get_pokemon(pid))
			#	pokemon = {'id': pid, 'name' : movie[0], 'type' : movie[1]}
			#	output['pokemon'].append(dpokemon) 		JSON format check

		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	def POST_INDEX(self):
		output = { 'result' : 'success'}
		data = json.loads(cherrypy.request.body.read().decode('utf-8'))

		try:
			newID = int(self.pdb.pokemon_data[-1]['id']) + 1
			self.pdb.pokemon_data.append(dict())
			self.pdb.pokemon_data[newID-1]['id'] = newID
			self.pdb.pokemon_data[newID-1]['name'] = dict()
			self.pdb.pokemon_data[newID-1]['name']['english'] = data['name']
			self.pdb.pokemon_data[newID-1]['types'] = data['types']
			self.pdb.pokemon_data[newID-1]['image'] = data['image']
			self.pdb.pokemon_data[newID-1]['stats'] = "???"

			output['id'] = newID

		except Exception as ex:
			output['result'] = 'failure'
			output['message'] = str(ex)

		return json.dumps(output)



	def DELETE_INDEX(self):
		output = {'result' : 'success'}

		try:
			allPokemon = list(self.mdb.get_pokemon())
			for pID in allPokemon:
				self.mdb.delete_pokemon(pID)

		except Exception as ex:
			output['result'] ='failure'
			output['message'] = str(ex)

		return json.dumps(output)

