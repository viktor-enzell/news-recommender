import settings

ITEM_PIPELINES = {
    'scrapyelasticsearch.scrapyelasticsearch.ElasticSearchPipeline': 500
}

ELASTICSEARCH_SERVERS = ['localhost:9200']
ELASTICSEARCH_INDEX = INDEX
ELASTICSEARCH_TYPE = 'items'

DEPTH_LIMIT = 4
