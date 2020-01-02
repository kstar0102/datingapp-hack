import scrapy


class PostItem(scrapy.Item):
    id = scrapy.Field()
    profile_id = scrapy.Field()
    name = scrapy.Field()
    age = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    image_url = scrapy.Field()
    post_at = scrapy.Field()
    genre = scrapy.Field()
    prefecture = scrapy.Field()
    city = scrapy.Field()
