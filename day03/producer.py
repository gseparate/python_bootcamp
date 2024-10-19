from random import randint
import json 
import logging
import time
from redis import StrictRedis

def generate_data():
    result = dict({'metadata' : dict({'from' : randint(1000000000, 9999999999), 'to' : randint(1000000000, 9999999999)}), 'amount' : randint(-10000000, 10000000)})
    # result = dict({'metadata' : dict({'from' : randint(1, 9), 'to' : randint(1, 9)}), 'amount' : randint(-10000000, 10000000)})
    return json.dumps(result)


r = StrictRedis()
while True:
    r.publish('channel', generate_data())
    time.sleep(1)

