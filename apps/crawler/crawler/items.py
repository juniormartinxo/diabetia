import scrapy


class PageItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    raw_html = scrapy.Field()
