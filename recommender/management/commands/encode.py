from elasticsearch import Elasticsearch
import json
from django.core.management.base import BaseCommand
from gensim.models.doc2vec import Doc2Vec

es = Elasticsearch(hosts=["localhost"])

class Command(BaseCommand):
    """
    To run the command: ./manage.py crawl
    """

    def handle(self, *args, **options):
        """ Update scrapy index
        """
        model = Doc2Vec.load('./d2v.model')
        search_body = {
            "size": 10000,
            "query": {
                "match_all": {}
            }
        }
        res = es.search(index="scrapy-2021-04", body=search_body)
        hits = res['hits']['hits']

        for doc in hits:
            update_body = {
                "doc": {
                    "vector": model.infer_vector(doc['_source']['text'].split())
                }
            }

            es.update(index="scrapy-2021-04", id=doc['_id'], body=update_body)
