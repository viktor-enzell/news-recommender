from django.core.management.base import BaseCommand
from elasticsearch import Elasticsearch
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.parsing.preprocessing import remove_stopwords
from gensim.utils import simple_preprocess
from gensim.parsing.porter import PorterStemmer
from jsonstream import loads
from modelsettings import *

class Command(BaseCommand):
    """
    To run the command: ./manage.py train_model
    """

    def handle(self, *args, **options):
        data = []
        with open('./es/articles.json', encoding='utf8') as f:
            it = loads(f.read())
            data = list(it)

        data = [x['_source']['text'] for x in data]
        data = [remove_stopwords(x) for x in data]
        # list(map(lambda x: x['_source']['text'], data))
        data = [simple_preprocess(x, deacc=True) for x in data]
        porter_stemmer = PorterStemmer()
        data = [[porter_stemmer.stem(word) for word in x] for x in data]
        print(len(data))
        documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(data)]
        self.train_model(documents)

        return

    def train_model(self, tagged_data):
        model = Doc2Vec(tagged_data, vector_size=DIMS, min_count=2, max_vocab_size=None, workers=8, epochs=100)

        model.save(MODEL)
        print("Model Saved")
