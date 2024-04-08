import time
import scrapy
# 引入定義好的 PttPostItem 類別
from ptt_home_sale.items import PttPostItem

class PttHomeSaleSpider(scrapy.Spider):
    name = "home_sale"
    allowed_domains = ["ptt.cc"]
    start_urls = ["https://www.ptt.cc/bbs/home-sale/index.html"]

    def parse(self, response):
        # 取出上一頁網址，也可以自行定義網頁網址
        next_page = response.css('.wide::attr(href)').getall()[1]
        posts = response.css('.r-ent')
        for post in posts:
            # 每篇文章都是一個 PttPostItem 物件
            item = PttPostItem()
            title = post.css('.title a::text').get()
            author = post.css('.author::text').get()
            date = post.css('.date::text').get().strip()
            url = post.css('.title a::attr(href)').get()
            if date == '3/14':
                self.stop_crawling = True
                break
            # 設定屬性值
            item['title'] = title
            item['author'] = author
            item['date'] = date
            item['url'] = url
            print(title, author, date, url)
            # 使用 yield 將函式轉換成 `generator` 產生器
            yield item
        print(next_page)
        
        if not self.stop_crawling:
            # 讓爬蟲可以暫停休息幾秒繼續，避免太暴力爬取網站造成網站負擔
            time.sleep(3)
            # 讓爬蟲可以繼續發出網路請求爬取下一頁資料並解析內容
            yield response.follow(next_page,  self.parse)

        