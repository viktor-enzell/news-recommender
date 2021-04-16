class ElasticSearchPipeline(object):
    def process_item(self, item, spider):
        item.save()
        yield item
