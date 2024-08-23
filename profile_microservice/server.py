import grpc
from concurrent import futures
from post_pb2 import (Post,
                      CreatePostRequest,
                      CreatePostResponse,
                      ReadPostRequest,
                      ReadPostResponse,
                      GetPostsResponse,
                      GetPostsRequest)
import post_pb2_grpc


class ProfileService(post_pb2_grpc.ProfileServiceServicer):
    def GetProfile(self, request, context):
        print("Got request")
        information = post_stub.GetPosts(GetPostsRequest(user_id=request.user_id))
        print(information)
        # print("llll")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    post_pb2_grpc.add_ProfileServiceServicer_to_server(ProfileService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    channel = grpc.insecure_channel('localhost:50051')
    post_stub = post_pb2_grpc.PostServiceStub(channel)
    print("done")
    serve()
