import cherrypy
from pokemonController import PokemonController
from resetController import ResetController
from pokemon_library import _pokemon_database

def start_service():
    dispatcher = cherrypy.dispatch.RoutesDispatcher()

    pdb = _pokemon_database()

    pokemonController = PokemonController(pdb=pdb)
    resetController = ResetController(pdb=pdb)
    typeController = typeController(pdb=pdb)

    dispatcher.connect('pokemon_get', '/pokemon/:pokemon_name', controller=pokemonController, action = 'GET_KEY', conditions=dict(method=['GET']))
    dispatcher.connect('pokemon_put', '/pokemon/:pokemon_name', controller=pokemonController, action = 'PUT_KEY', conditions=dict(method=['PUT']))
    dispatcher.connect('pokemon_delete', '/pokemon/:pokemon_name', controller=pokemonController, action = 'DELETE_KEY', conditions=dict(method=['DELETE']))
    dispatcher.connect('pokemon_index_get', '/pokemon/', controller=pokemonController, action = 'GET_INDEX', conditions=dict(method=['GET']))
    dispatcher.connect('pokemon_index_post', '/pokemon/', controller=pokemonController, action = 'POST_INDEX', conditions=dict(method=['POST']))
    dispatcher.connect('pokemon_index_delete', '/pokemon/', controller=pokemonController, action = 'DELETE_INDEX', conditions=dict(method=['DELETE']))

    dispatcher.connect('reset_put', '/reset/:pokemon_name', controller=resetController, action = 'PUT_KEY', conditions=dict(method=['PUT']))
    dispatcher.connect('reset_index_put', '/reset/', controller=resetController, action = 'PUT_INDEX', conditions=dict(method=['PUT']))


    conf = {
            'global' : {
                'server.thread_pool': 5,
                'server.socket_host' : 'localhost',
                'server.socket_port': 51055
            },
    '/': {
            'request.dispatch' : dispatcher,
            }
    }

    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)


    if __name__ == '__main__':
        start_service()
