import cherrypy
import re, json
from pokemon_library import _pokemon_database

class RatingsController(object):

	def __init__(self, pdb=None):
		if pdb is None:
			self.pdb= _pokemon_database()
		#	self.pdb.load_ratings('ratings.dat') will need to change this
		else:
			self.pdb = pdb

	def GET_KEY(self, pokemon_id):
		output = {'result' : 'success'}
		pokemon_id = int(pokemon_id)
		output['pokemon_id'] = pokemon_id
		output['rating'] = self.pdb.get_rating(pokemon_id)

		return json.dumps(output)
