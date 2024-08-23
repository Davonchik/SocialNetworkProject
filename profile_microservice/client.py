import grpc
from post_pb2_grpc import ProfileServiceStub
from post_pb2 import GetProfileRequest

channel = grpc.insecure_channel('localhost:50051')
client = ProfileServiceStub(channel)

request = GetProfileRequest(user_id=1)
response = client.GetProfile(request)

print(response)
