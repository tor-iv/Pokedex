import cherrypy
from pokemonController import PokemonController
from resetController import ResetController
from pokemon_library import _pokemon_database
from typeController import TypeController

def start_service():
    dispatcher = cherrypy.dispatch.RoutesDispatcher()

    pdb = _pokemon_database()

    pokemonController = PokemonController(pdb=pdb)
    resetController = ResetController(pdb=pdb)
    typeController = TypeController(pdb=pdb)

    dispatcher.connect('pokemon_get', '/pokemon/:pokemon_name', controller=pokemonController, action = 'GET_KEY', conditions=dict(method=['GET']))
    dispatcher.connect('pokemon_put', '/pokemon/:pokemon_name', controller=pokemonController, action = 'PUT_KEY', conditions=dict(method=['PUT']))
    dispatcher.connect('pokemon_delete', '/pokemon/:pokemon_name', controller=pokemonController, action = 'DELETE_KEY', conditions=dict(method=['DELETE']))
    dispatcher.connect('pokemon_index_get', '/pokemon/', controller=pokemonController, action = 'GET_INDEX', conditions=dict(method=['GET']))
    dispatcher.connect('pokemon_index_post', '/pokemon/', controller=pokemonController, action = 'POST_INDEX', conditions=dict(method=['POST']))
    dispatcher.connect('pokemon_index_delete', '/pokemon/', controller=pokemonController, action = 'DELETE_INDEX', conditions=dict(method=['DELETE']))

    dispatcher.connect('reset_put', '/reset/:pokemon_name', controller=resetController, action = 'PUT_KEY', conditions=dict(method=['PUT']))
    dispatcher.connect('reset_index_put', '/reset/', controller=resetController, action = 'PUT_INDEX', conditions=dict(method=['PUT']))

    dispatcher.connect('pokemon_options', '/pokemon/', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('pokemon_key_options', '/pokemon/:pokemon_name', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))

    conf = {
            'global' : {
                'server.thread_pool': 5,
                'server.socket_host' : 'localhost',
                'server.socket_port': 51055
            },
    '/': {
            'request.dispatch' : dispatcher,
            'tools.CORS.on' : True, # configuration for CORS
        }
    }

    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)

# class for CORS
class optionsController:
    def OPTIONS(self, *args, **kwargs):
        return ""

# function for CORS
def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE"
    cherrypy.response.headers["Access-Control-Allow-Credentials"] = "true"




if __name__ == '__main__':
    cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS) # CORS
    start_service()
