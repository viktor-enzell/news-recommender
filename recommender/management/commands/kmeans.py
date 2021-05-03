import numpy as np
from sklearn.cluster import KMeans
from elasticsearch import Elasticsearch
from django.core.management.base import BaseCommand

es = Elasticsearch(hosts=["localhost"])

class Command(BaseCommand):
    """
    To run the command: ./manage.py crawl
    """

    def handle(self, *args, **options):
        body = {
            "size": 10000,
            "query": {
                "match_all": {}
            }
        }
        data = es.search(index="scrapy-2021-04", body=body)['hits']['hits']
        d = [x['_source']['title'] for x in data]
        x = np.array(list(map(lambda x: x['_source']['vector'], data)))
        kmeans = KMeans(n_clusters=40).fit(x)
        res = np.where(kmeans.labels_ == 15)[0]
        for i in res:
            print(d[i])
