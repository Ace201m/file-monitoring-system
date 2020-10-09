import pymongo
from .names import Names


class Database:

    def __init__(self):
        myClient = pymongo.MongoClient(Names.SERVER_CONNECT)
        db = myClient[Names.DBNAME]

        self.col = dict()
        self.col[Names.DB_DATA_COLLECTION] = db[Names.DB_DATA_COLLECTION]
        self.col[Names.DB_ACTION_COLLECTION] = db[Names.DB_ACTION_COLLECTION]

    def insert(self, collection, data):
        verdict = self.col[collection].insert_one(data)
        if not verdict.acknowledged:
            raise Exception('data not inserted')
        return True

    def update(self, collection, path, data):
        self.col[collection].update_one({'_id': path}, data)

    def delete(self, collection, path):
        self.col[collection].delete_one({'_id': path})

    def get(self, collection, path):
        return self.col[collection].find_one({Names.DB_DATA_COLLECTION_PATH: path})
