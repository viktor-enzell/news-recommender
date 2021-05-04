from django.core.management.base import BaseCommand
from elasticsearch import Elasticsearch
import numpy as np
from modelsettings import *


class Command(BaseCommand):
    """
    Create predefined users.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.elastic_client = Elasticsearch(hosts=["localhost"])
        self.user_names = ['Sanna', 'Tim', 'Adam', 'Viktor']

    def handle(self, *args, **options):
        # Retrieve all article vectors to initialize like centroid to the average of all article vectors
        results = self.elastic_client.search(index=INDEX, size=10000)
        all_article_vectors = []
        for result in results['hits']['hits']:
            all_article_vectors.append(result['_source']['vector'])

        # Set like centroid to the centroid of all articles
        like_centroid = list(np.average(all_article_vectors, axis=0))
        # Set dislike centroid to zero vector
        dislike_centroid = np.zeros(DIMS)

        for i, name in enumerate(self.user_names):
            user = {
                'name': name,
                'liked_articles': [],
                'disliked_articles': [],
                'like_centroid': like_centroid,
                'dislike_centroid': dislike_centroid
            }
            result = self.elastic_client.index(index='users', id=i, body=user)
            print(f'Creating user {name} result: {result["result"]}')
