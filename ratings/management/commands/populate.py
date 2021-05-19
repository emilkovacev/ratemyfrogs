from django.core.management.base import BaseCommand, CommandError
from ratings.models import Frog
import requests
import sys


def get_frogs(page, page_size):
    response = requests.get('https://api.creativecommons.engineering/v1/images',
    params={'q': 'frog', 'license': 'CC0,PDM', 'page': str(page), 'page_size': str(page_size)})
    if response.status_code != 200:
        raise CommandError
    return response.json()


class RePopulationError(Exception):
    sys.tracebacklimit = 0
    pass


class Command(BaseCommand):
    help='populate database with frogs from CC library'
    
    def add_arguments(self, parser):
        parser.add_argument('page_number', type=int,
                            help='page number of frog query')
        parser.add_argument('page_size', type=int,
                            help='number of entries per page on query', default=50)
    
    def handle(self, *args, **kwargs):
        # page_number and page_size
        frogs = get_frogs(kwargs['page_number'], kwargs['page_size'])
        for f in frogs['results']:
            if Frog.objects.filter(title=f['title'], url=f['url']).exists():
                raise RePopulationError(f"Invalid request to repopulate page {kwargs['page_number']}")
            frog = Frog(title=f['title'], url=f['url'])
            frog.save()
 
        self.stdout.write(self.style.SUCCESS(f"Successfully added {kwargs['page_size']} frogs"))
