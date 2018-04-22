from pymongo import MongoClient
from bson.objectid import ObjectId
import mongodb.connectionstring as cs
import json as js

class mongoconnect:
    def __init__(self):
        try:
            self.client = MongoClient(cs.MONGO_CONNECTION)
            self.db = self.client[cs.MONGO_DB]
        except Exception as ex:
            print(ex)

    def insert(self,json,collectionname):
        cn=self.db[collectionname]
        try:
            modelid=cn.insert_one(json).inserted_id
            print("Data inserted successfully"+" "+str(modelid))
        except Exception as ex:
            print(ex)
        return modelid

    def find(self,json,collectionname,id):
        cn=self.db[collectionname]
        try:
            document=cn.find_one({'_id': ObjectId(id)})
        except Exception as ex:
            print(ex)

        return document






        