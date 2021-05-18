from django.core.management.base import BaseCommand, CommandError
from ratings.models import Frog
import requests

def get_frogs():
        response = requests.get('https://api.creativecommons.engineering/v1/images',
        params={'q': 'frog', 'license': 'CC0', 'page': '1', 'page_size': '20'})
        return response.json()

def load_frogs():
    frogs = get_frogs()
    for f in frogs['results']:
        print(f)
        frog = Frog(title=f['title'], url=f['url'])
        frog.save()

class Command(BaseCommand):
    help='populate frog database'
    
    def handle(self, *args, **options):
        load_frogs()
        self.stdout.write(self.style.SUCCESS('Successfully added 20 frogs'))
