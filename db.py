from pymongo import MongoClient
import random


client = MongoClient('localhost', connect=False)
db = client['frogs']
collection = db['ratings']


def get_frogs_by_url(url):
    return collection.find_one({'url': url})

# total, n are collections of the average (total / n)
def add_frog(url, total=0, n=0):
    collection.insert_one({'url': url, 'total': total, 'n': n})

def increment_frog(url, rating):
    frog = collection.find_one({'url': url})
    if frog:
        collection.update_one(
            {'url': url},
            {
                '$set': {
                    'total': frog['total'] + rating, 
                    'n': frog['n'] + 1 
                }
            })
    else:
        add_frog(url, rating, 1)
