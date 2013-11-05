from ZenPacks.community.ConstructionKit.ClassHelper import *

def MongoDBgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class MongoDBInfo(ClassHelper.MongoDBInfo):
    ''''''


