from django.core.management.base import BaseCommand
from elasticsearch import Elasticsearch
from gensim.models.doc2vec import Doc2Vec, TaggedDocument


class Command(BaseCommand):
    """
    To run the command: ./manage.py train_model
    """

    def handle(self, *args, **options):
        elastic_client = Elasticsearch(hosts=["localhost"])
        body = {
            "size": 5000,
            "query": {
                "match_all": {}
            }
        }
        data = elastic_client.search(index="scrapy-2021-04", body=body)['hits']['hits']
        data = list(map(lambda x: x['_source']['text'], data))
        documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(data)]
        self.train_model(documents)

        return

    def train_model(self, tagged_data):
        model = Doc2Vec(tagged_data, vector_size=10, window=2, min_count=1, workers=4)

        model.save("d2v.model")
        print("Model Saved")
