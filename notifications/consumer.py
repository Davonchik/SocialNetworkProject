import os
from kafka import KafkaConsumer
import jwt
import json

KAFKA_BOOTSTRAP_SERVERS = os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "localhost:29092")
KAFKA_TOPIC_TEST = os.environ.get("KAFKA_TOPIC_TEST", "test")
KAFKA_API_VERSION = os.environ.get("KAFKA_API_VERSION", "7.3.1")
consumer = KafkaConsumer(
    KAFKA_TOPIC_TEST,
    bootstrap_servers=[KAFKA_BOOTSTRAP_SERVERS],
    api_version=KAFKA_API_VERSION,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
)
for message in consumer:
    a = message.value.decode("utf-8")
    a = json.loads(a)
    token = ''
    if "access_token" in a:
        token = a['access_token']
        SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
        ALGORITHM = "HS256"
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            decoded_token: str = payload.get("sub")
            print(decoded_token)
        except jwt.ExpiredSignatureError:
            print("token expired")
