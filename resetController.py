import cherrypy
import re, json
from pokemon_library import _pokemon_database

class ResetController(object):

	def __init__(self, pdb=None):
		if pdb is None:
			self.pdb = _pokemon_database()
		else:
			self.pdb = pdb

	def PUT_INDEX(self):
		output = {'result' : 'success'}

		data = json.loads(cherrypy.request.body.read().decode())

		self.pdb.__init__()
		self.pdb.load_pokemon('pokemon.json')
		#self.pdb.load_ratings('ratings.dat') replace with images or seperate type file?

		return json.dumps(output)

	def PUT_KEY(self, pokemon_id):
		output = {'result' : 'success'}
		pid = str(pokemon_id)

		try:
			data = json.loads(cherrypy.request.body.read().decode())

			pdbtmp = _pokemon_database()
			pdbtmp.load_pokemon('pokemon.json')

			pokemon = pdbtmp.get_pokemon(pid)
			
			self.pdb.set_pokemon(pid, pokemon)

		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)
