from pymongo import MongoClient

class DataManager(object):
    def __init__(self, server_address, port):
        mongodb = MongoClient(server_address, port)
        self.db = mongodb.word
        self.col = self.db['word']

    def save(self, instance):
        print type(instance)
        result = self.col.find_one({'text' : instance['text']})
        if result == None:
            self.col.insert(instance)

    def find(self, condition={}):
        return self.col.find(condition)