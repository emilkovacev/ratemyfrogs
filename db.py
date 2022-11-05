from pymongo import MongoClient

client = MongoClient('localhost', connect=False)
db = client['frogs']
collection = db['ratings']


def get_frogs_by_url(url):
    return collection.find_one({'url': url})

# total, n are collections of the average (total / n)
def add_frog(url, total=0, n=0):
    assert type(total) == int
    assert type(n) == int

    avg = int(total) / int(n)
    collection.insert_one({'url': url, 'total': total, 'n': n, 'avg': avg})

def increment_frog(url, rating):
    assert type(url) == str
    assert type(rating) == int

    frog = collection.find_one({'url': url})
    if frog:
        total, n = int(frog['total']), int(frog['n'])
        avg = (total + rating) / (n + 1)
        collection.update_one(
            {'url': url},
            {'$set': {
                'total': total + rating, 
                'n': n + 1,
                'avg': avg
            }})
    else:
        add_frog(url, rating, 1)

def get_most_popular():
    popular = list(collection.find().sort([('avg', -1), ('n', -1)]).limit(3))
    if len(popular) >= 3:
        return [x['url'] for x in popular]
    else:
        return None

def get_frogs():
    return list(collection.find())
