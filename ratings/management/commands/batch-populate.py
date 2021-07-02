from django.core.management.base import BaseCommand, CommandError
from ratings.models import Frog
from .populate import get_frogs, populate, RePopulationError
import requests
import sys


class Command(BaseCommand):
    help='batch populate database with frogs from CC library'
    
    def add_arguments(self, parser):
        parser.add_argument('request_size', type=int,
                            help='number of frogs to add to database')
        parser.add_argument('-f', '--force', action='store_true',
                            help='saves all non-conflicting frogs to database')
    
    def handle(self, *args, **kwargs):
        # command-line arguments
        request_size = kwargs['request_size']
        force = kwargs['force']
        
        page_number = 1
        page_size = min(500, request_size)
        added = 0
        while request_size > 0 and page_number < 5:
            if request_size < page_size:
                page_size -= 1
            else:
                added_frogs = populate(page_number, page_size, force) 
                page_number += 1
                added += added_frogs
                request_size =- added

        self.stdout.write(self.style.SUCCESS(f"Successfully added {added} frogs"))
