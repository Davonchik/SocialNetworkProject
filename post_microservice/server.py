import grpc
from concurrent import futures
from post_pb2 import (Post,
                      CreatePostRequest,
                      CreatePostResponse,
                      ReadPostRequest,
                      ReadPostResponse,
                      GetPostsResponse)
import post_pb2_grpc


class PostService(post_pb2_grpc.PostServiceServicer):
    def CreatePost(self, request, context):
        print(request.title)
        post = Post(id=request.id, title=request.title,
                    content=request.content, timestamp=request.timestamp,
                    user_id=request.user_id)
        return CreatePostResponse(post=post)

    def GetPosts(self, request, context):
        print(request.user_id)
        post1 = Post(id=request.user_id, title="bla",
                    content="bla bla", timestamp="23456",
                    user_id=21)
        post2 = Post(id=request.user_id, title="lala",
                     content="lalala", timestamp="11111",
                     user_id=23)
        posts = GetPostsResponse()
        posts.posts.extend([post1, post2])
        return posts


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    post_pb2_grpc.add_PostServiceServicer_to_server(PostService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
