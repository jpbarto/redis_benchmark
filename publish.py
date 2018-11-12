import redis
import json
import uuid

HOST = 'localhost'
PORT = 6379
MSG_COUNT = 10000

r = redis.Redis (host = HOST, port = PORT)
pub = r.pubsub ()

sender_id = uuid.uuid4 ()

for i in range (MSG_COUNT):
    data = {"sender_id": str(sender_id), "message_id": i, "body": "I am message number {}".format (i)}
    r.publish ('a_topic', json.dumps (data))

print ("Published {} messages with sender ID {}".format (MSG_COUNT, sender_id))
