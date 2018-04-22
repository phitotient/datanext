from protos import ModelService_pb2_grpc
from protos import ModelService_pb2
from models.savemodel import savemodel


class ModelService(ModelService_pb2_grpc.ModelServiceServicer):
    def __init__(self):
        self.sm=savemodel()


    def Save(self, request, context):
        modelid=self.sm.savemodel(request)
        return ModelService_pb2.SaveReply()

    def Run(self, request, context):
        return ModelService_pb2.RunReply()

    def Health(self, request, context):
        return ModelService_pb2.HealthReply()

    def Rebuild(self, request, context):
        return ModelService_pb2.RebuildReply()


    def Visualize(self, request, context):
        return ModelService_pb2.VisualizeReply()

    def Load(self, request, context):
        return ModelService_pb2.LoadReply()
