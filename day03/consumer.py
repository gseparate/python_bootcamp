import argparse
import redis
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
def print_transactions(transaction, bad_guys_list):

    if(str(transaction['metadata']['to']) in bad_guys_list and transaction['amount'] > 0):
        transaction['metadata']['from'], transaction['metadata']['to'] = transaction['metadata']['to'], transaction['metadata']['from']
    logging.info(transaction)

parser = argparse.ArgumentParser(description='get json script of transaction')
parser.add_argument('-e', type=str, dest='bad_guys')
args = parser.parse_args()
bad_guys_list = list(str(args.bad_guys).split(','))

r = redis.StrictRedis()
pubsub = r.pubsub()
pubsub.subscribe('channel')

for message in pubsub.listen():
    if message['type'] == 'message':
        print_transactions(json.loads(message['data']), bad_guys_list)