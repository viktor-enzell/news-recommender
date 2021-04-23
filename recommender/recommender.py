from elasticsearch import Elasticsearch
import json


class Recommender:
    """
    Recommendation engine. Recommend articles stored in ES.
    """

    def __init__(self):
        self.elastic_client = Elasticsearch(hosts=["localhost"])

    def search(self, query, query_type):
        body = {
            "query": {
                "match": {
                    "text": {
                        "query": query,
                        "fuzziness": "AUTO",
                        "operator": query_type
                    }
                }
            }
        }
        res = self.elastic_client.search(index="scrapy-2021-04", body=body, size=10)
        return res['hits']['hits']

    def recommend_articles(self, user_id, query):
        print(f'user {user_id} searched for {query}')
        result = self.search(query, '')
        articles = []
        for item in result:
            article = item['_source']
            article['id'] = item['_id']
            articles.append(article)
        return articles

    def like_article(self, user_id, article_id):
        print(f'User {user_id} liked article {article_id}')
        liked_articles, disliked_articles = self.get_reviewed_articles(user_id)
        if article_id in liked_articles:
            # Do nothing if user has already liked article
            return
        if article_id in disliked_articles:
            # Remove article from disliked articles
            self.elastic_client.update(
                index='users',
                id=user_id,
                body={
                    'script': {
                        'source': f'ctx._source.disliked_articles'
                                  f'.remove(ctx._source.disliked_articles.indexOf(params.disliked_articles))',
                        'lang': 'painless',
                        'params': {
                            'disliked_articles': article_id
                        }
                    }
                }
            )
        # Add article to liked articles
        self.elastic_client.update(
            index='users',
            id=user_id,
            body={
                'script': {
                    'source': 'ctx._source.liked_articles.add(params.liked_articles)',
                    'lang': 'painless',
                    'params': {
                        'liked_articles': article_id
                    }
                }
            }
        )

    def dislike_article(self, user_id, article_id):
        print(f'User {user_id} disliked article {article_id}')
        liked_articles, disliked_articles = self.get_reviewed_articles(user_id)
        if article_id in disliked_articles:
            # Do nothing if user has already disliked article
            return
        if article_id in liked_articles:
            # Remove article from liked articles
            self.elastic_client.update(
                index='users',
                id=user_id,
                body={
                    'script': {
                        'source': f'ctx._source.liked_articles'
                                  f'.remove(ctx._source.liked_articles.indexOf(params.liked_articles))',
                        'lang': 'painless',
                        'params': {
                            'liked_articles': article_id
                        }
                    }
                }
            )
        # Add article to disliked articles
        self.elastic_client.update(
            index='users',
            id=user_id,
            body={
                'script': {
                    'source': 'ctx._source.disliked_articles.add(params.disliked_articles)',
                    'lang': 'painless',
                    'params': {
                        'disliked_articles': article_id
                    }
                }
            }
        )

    def get_users(self):
        result = self.elastic_client.search(index='users')
        users = [('no_user_selected', 'No user selected')]

        for user in result['hits']['hits']:
            users.append((user['_id'], user['_source']['name']))

        return users

    def get_reviewed_articles(self, user_id):
        result = self.elastic_client.search(
            index='users',
            body={
                'query': {
                    'match': {
                        '_id': user_id
                    }
                }
            }
        )
        source = result['hits']['hits'][0]['_source']
        return source['liked_articles'], source['disliked_articles']
