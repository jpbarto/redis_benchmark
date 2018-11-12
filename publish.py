import redis
import json
import uuid
import time

HOST = 'localhost'
PORT = 6379
MSG_COUNT = 250000

r = redis.Redis (host = HOST, port = PORT)
pub = r.pubsub ()

sender_id = uuid.uuid4 ()

start_time = time.time ()
for i in range (MSG_COUNT):
    data = {"sender_id": str(sender_id), "message_id": i, "body": "I am message number {}".format (i)}
    r.publish ('a_topic', json.dumps (data))
end_time = time.time ()
print ("Published {} messages with sender ID {} in {} seconds".format (MSG_COUNT, sender_id, (end_time - start_time)))
