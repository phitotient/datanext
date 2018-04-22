from google.protobuf.json_format import MessageToJson
from mongodb.mongoconnect import mongoconnect
import json

class savemodel:

    def __init__(self):
        self.mc=mongoconnect()

    def savemodel(self,request):
        ModelName=request.name
        SourceKey=request.sourceKey
        self.mc.insert({"name":ModelName,"sourcekey":SourceKey,},"modelsinfo")

    def updatemodel(self,request):
        pass