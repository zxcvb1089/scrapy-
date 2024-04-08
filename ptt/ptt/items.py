# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PttPostItem(scrapy.Item):
    # 使用 scrapy.Field() 定義類別屬性內容，之後會將抓取的內容設定為物件屬性
    title = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    url = scrapy.Field()