from django.core.management.base import BaseCommand
from scrapy.cmdline import execute
import pathlib

path = pathlib.Path(__file__).parent.absolute()

class Command(BaseCommand):
    """
    To run the command: ./manage.py crawl
    """

    def handle(self, *args, **options):
        print('Crawl the web for stuff and store in ES')
        execute(['', 'runspider', str(path) + '/spooder.py'])
