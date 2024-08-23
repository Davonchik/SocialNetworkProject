import grpc
from post_pb2_grpc import PostServiceStub
from post_pb2 import CreatePostRequest, GetPostsRequest

channel = grpc.insecure_channel('localhost:50051')
client = PostServiceStub(channel)

request = GetPostsRequest(user_id=500)
response = client.GetPosts(request)

print(response)
