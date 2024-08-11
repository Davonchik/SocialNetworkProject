from fastapi import FastAPI
from pydantic import BaseModel
import grpc
from post_pb2_grpc import PostServiceStub
from post_pb2 import CreatePostRequest

channel = grpc.insecure_channel('localhost:50051')
client = PostServiceStub(channel)

app = FastAPI()


class PostModel(BaseModel):
    id: int
    title: str
    content: str
    timestamp: str
    user_id: int

# func - converting from proto to json

@app.post('/create_post')
def create_post(post: PostModel):
    request = CreatePostRequest(id=post.id, title=post.title,
                                content=post.content, timestamp=post.timestamp,
                                user_id=post.user_id)
    response = client.CreatePost(request)
    print(response)
    return {"status": "ok"}
