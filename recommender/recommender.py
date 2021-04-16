from elasticsearch import Elasticsearch

class Recommender:
    """
    Recommendation engine. Recommend articles stored in ES.
    """
    def __init__(self):
        self.elastic_client = Elasticsearch(hosts=["localhost"])

    def recommend_articles(self, user_id, query, search_type):
        return self.search(query, search_type)

    def search(self, query, search_type):
        # Constructs simple query
        matches = []
        for s in query.split(" "):
            matches.append({ "match": { "text": s}})
        
        body = {
                "query": {
                    "bool": {
                        search_type: matches
                        }
                    }
                }
        res = self.elastic_client.search(index="scrapy", body=body)
        return res['hits']['hits']
        



