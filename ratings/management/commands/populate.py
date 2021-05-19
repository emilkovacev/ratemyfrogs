from django.core.management.base import BaseCommand, CommandError
from ratings.models import Frog
import requests
import sys


def get_frogs(page, page_size):
    if page_size > 500:
        raise CommandError

    response = requests.get('https://api.creativecommons.engineering/v1/images',
    params={'q': 'frog', 'license': 'CC0,PDM', 'size': 'medium,large', 'page': str(page), 'page_size': str(page_size)})
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
        parser.add_argument('-f', '--force', action='store_true',
                            help='saves all non-conflicting frogs to database')
    
    def handle(self, *args, **kwargs):
        # command-line arguments
        page_number = kwargs['page_number']
        page_size = kwargs['page_size']
        force = kwargs['force']

        frogs = get_frogs(page_number, page_size)
        i = 0

        for f in frogs['results']:
            exists = Frog.objects.filter(title=f['title'], url=f['url']).exists()
            if not force and exists:
                raise RePopulationError(f"Page {kwargs['page_number']} is already populated")
            elif not exists:
                i += 1
                frog = Frog(title=f['title'], url=f['url'])
                frog.save()
 
        self.stdout.write(self.style.SUCCESS(f"Successfully added {i} frogs"))
