from elasticsearch import Elasticsearch
from django.core.management.base import BaseCommand
from gensim.models.doc2vec import Doc2Vec
from gensim.parsing.preprocessing import remove_stopwords
from gensim.utils import simple_preprocess
from gensim.parsing.porter import PorterStemmer
from modelsettings import *

es = Elasticsearch(hosts=["localhost"])

class Command(BaseCommand):
    """
    To run the command: ./manage.py encode
    """

    def handle(self, *args, **options):
        """ Update scrapy index
        """
        # mapping = {
        #     "properties": {
        #         "vector": {
        #             "type": "dense_vector",
        #             "dims": DIMS
        #         }
        #     }
        # }
        # es.indices.put_mapping(mapping, index=INDEX)

        model = Doc2Vec.load(MODEL)
        search_body = {
            "size": 10000,
            "query": {
                "match_all": {}
            }
        }
        res = es.search(index=INDEX, body=search_body)
        hits = res['hits']['hits']
        porter_stemmer = PorterStemmer()

        for doc in hits:
            data = remove_stopwords(doc['_source']['text'])
            data = simple_preprocess(data, deacc=True)
            data = [porter_stemmer.stem(word) for word in data]

            update_body = {
                "doc": {
                    "vector": model.infer_vector(data)
                }
            }

            es.update(index=INDEX, id=doc['_id'], body=update_body)
