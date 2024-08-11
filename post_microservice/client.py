import grpc
from post_pb2_grpc import PostServiceStub
from post_pb2 import CreatePostRequest

channel = grpc.insecure_channel('localhost:50051')
client = PostServiceStub(channel)

request = CreatePostRequest(id=1, title="Tennis", content="About the game", timestamp="2024.08.11", user_id=500)
response = client.CreatePost(request)

print(response)