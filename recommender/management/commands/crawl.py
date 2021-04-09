from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    To run the command: ./manage.py crawl
    """

    def handle(self, *args, **options):
        print('Crawl the web for stuff and store in ES')
