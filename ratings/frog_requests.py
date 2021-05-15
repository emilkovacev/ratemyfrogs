import requests
from ratings.models import Frog


def get_frogs():
    response = requests.get('https://api.creativecommons.engineering/v1/images', 
    params={'q': 'frog', 'license': 'CC0', 'page': '1', 'page_size': '500'})
    return response.json()


def load_frogs(): 
    frogs = get_frogs()
    print(frogs)
    for f in frogs['results']: 
        frog = Frog(name=f['name'], frog=f['link'])
        frog.save()


if __name__ == '__main__':
    load_frogs()

