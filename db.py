from pymongo import MongoClient

client = MongoClient('localhost', connect=False)
db = client['frogs']
collection = db['ratings']


def get_frogs_by_url(url):
    return collection.find_one({'url': url})

# total, n are collections of the average (total / n)
def add_frog(url, total=0, n=0):
    avg = int(total) / int(n)
    collection.insert_one({'url': url, 'total': total, 'n': n, 'avg': avg})

def increment_frog(url, rating):
    frog = collection.find_one({'url': url})
    if frog:
        collection.update_one(
            {'url': url},
            {'$set': {
                'total': int(frog['total'] + rating), 
                'n': int(frog['n'] + 1),
                'avg': int(frog['total'] + rating) / int(frog['n'] + 1)
            }})
    else:
        add_frog(url, rating, 1)

def get_most_popular():
    popular = list(collection.find().sort('avg', -1))[0]
    return popular['url']
