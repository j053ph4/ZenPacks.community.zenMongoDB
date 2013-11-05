from ZenPacks.community.ConstructionKit.BasicDefinition import *
from ZenPacks.community.ConstructionKit.Construct import *               
                            
DATA = {
        'version' : Version(1, 1, 0),
        'zenpackbase': "zenMongoDB",
        'component' : 'MongoDB',
        'componentData' : {
                          'singular': 'Mongo DB',
                          'plural': 'Mongo DB',
                          'displayed': 'hostname', # component field in Event Console
                          'primaryKey': 'hostname',
                          'properties': { 
                                        # Basic settings
                                        'hostname' : addProperty('Hostname or IP','Basic','id', switch='-H', override=True, isReference=True),
                                        'port' : addProperty('Port','Basic','27017', switch='-p',optional='false'),
                                        'eventClass' : getEventClass('/App/MongoDB'),
                                        },
                          },
        'cmdFile' : 'check_mongo',
        'addManual' : True,
        }

MongoDBDefinition = type('MongoDBDefinition', (BasicDefinition,), DATA)

