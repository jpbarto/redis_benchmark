import redis
import time
import json

HOST = 'localhost'
PORT = 6379
MSG_COUNT = 1000

r = redis.Redis (host = HOST, port = PORT)
pub = r.pubsub ()

pub.subscribe ('a_topic')

last_message_ids = {}

while True:
    msg = pub.get_message ()
    if msg:
        if msg['type'] == 'message':
            body = json.loads (msg['data'])
            sender_id = body['sender_id']
            message_id = body['message_id']

            if sender_id not in last_message_ids:
                last_message_ids[sender_id] = -1
            expect_message_id = last_message_ids[sender_id] + 1

            if message_id != expect_message_id:
                print ("Error, message ID {}, received from sender {}, is out of order with last message {}, expected {}".format (message_id, sender_id, last_message_ids[sender_id], expect_message_id))

            last_message_ids[sender_id] = int(message_id)

            if message_id + 1 == MSG_COUNT:
                print ("Received {} messages from sender {}".format (MSG_COUNT, sender_id))

            # print ("Processed message {}: {}".format (message_id, body))
        else:
            print ("Got message: {}".format (msg))

