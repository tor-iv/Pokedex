import cherrypy
import re, json
from pokemon_library import _pokemon_database

class pokemonController(object):

	def __init__(self, mdb=None):
		if pdb is None:
			self.pdb = _pokemon_database()
		else:
			self.pdb = pdb

		self.pdb.load_pokemon('pokemon.json') # was movies.dat


	def GET_KEY(self, pokemon_id):
		output = {'result' : 'success'}
		pokemon_id = int(pokemon_id)

		try:
			pokemon = self.pdb.get_pokemon(pokemon_id)
			if pokemon is not None:
				output['id'] = pokemon_id
			#	output['title'] = movie[0] figure this out with JSON formatted file
			#	output['genres'] = movie[1]

			else:
				output ['result'] = 'error'
				output['message'] = 'movie not found'

		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	def PUT_KEY(self, pokemon_id):
		output = {'result' : 'success'}
		pokemon_id = int(pokemon_id)

		data = json.loads(cherrypy.request.body.read().decode('utf-8'))

		pokemon = list()
		pokemon.append(data['name'])
		pokemon.append(data['type'])

		self.pdb.set_pokemon(pokemon_id, pokemon)

		return json.dumps(output)

	def DELETE_KEY(self, pokemon_id):
		
		output = {'result' : 'success'}

		pokemon_id = int(pokemon_id)

		try:
			self.pdb.delete_pokemon(pokemon_id)
		except Exception as ex:
			output['result'] = 'failure'
			output['message'] = str(ex)

		return json.dumps(output)

	def GET_INDEX(self):
		output = {'result' : 'success'}
		output['movies'] = []

		try:
			for pid in self.pdb.get_pokemon():
				pokemon = self.pdb.get_pokemon(pid)
			#	dpokemon = {'id': pid, 'name' : movie[0], 'type' : movie[1]}
			#	output['pokemon'].append(dpokemon) 		JSON format check

		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	def POST_INDEX(self):
		output = { 'result' : 'success'}
		data = json.loads(cherrypy.request.body.read().decode('utf-8'))

		try:
			movies = sorted(list(self.mdb.get_movies()))
			newID = int(movies[-1]) + 1
			self.mdb.movie_names[newID] = data['title']
			self.mdb.movie_genres[newID] = data['genres']
			self.mdb.movie_ratings[newID] = dict()
			output['id'] = newID

		except Exception as ex:
			output['result'] = 'failure'
			output['message'] = str(ex)

		return json.dumps(output)



	def DELETE_INDEX(self):
		output = {'result' : 'success'}

		try:
			allMovies = list(self.mdb.get_movies())
			for movID in allMovies:
				self.mdb.delete_movie(movID)

		except Exception as ex:
			output['result'] ='failure'
			output['message'] = str(ex)

		return json.dumps(output)

