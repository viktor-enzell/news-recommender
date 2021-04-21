from django.core.management.base import BaseCommand
from elasticsearch import Elasticsearch


class Command(BaseCommand):
    """
    Create predefined users.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.elastic_client = Elasticsearch(hosts=["localhost"])
        self.user_names = ['Sanna', 'Tim', 'Adam', 'Viktor']

    def handle(self, *args, **options):
        for name in self.user_names:
            user = {
                'name': name,
                'liked_articles': [],
                'disliked_articles': [],
                'vector_representation': []
            }
            result = self.elastic_client.index(index='users', body=user)
            print(f'Creating user {name} result: {result["result"]}')
