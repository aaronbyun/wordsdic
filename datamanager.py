from pymongo import MongoClient

class DataManager(object):
    def __init__(self, server_address, port):
        mongodb = MongoClient(server_address, port)
        self.db = mongodb.word
        self.col = self.db['word']

    def save(self, instance):
        print type(instance)
        result = self.col.find({'text' : instance['text']})
        if not result.count() > 0:
            self.col.insert(instance)