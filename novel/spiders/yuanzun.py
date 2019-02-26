import scrapy
from novel.items import NovelItem
import logging

class YuanZun(scrapy.Spider):
    name = "yuanzun"

    start_urls = ['https://www.booktxt.net/6_6453/']

    # def parse(self, response):
    #     for quote in response.css("div#list dd a"):
    #         next_page = quote.css("a::attr(href)").get()
    #         yield {
    #             'url:': next_page,
    #             'name:': quote.css("a::text").get()
    #
    #         }

    def parse(self, response):
        # 获取所有子页面
        for quote in response.css("div#list dd a"):
            next_page = quote.css("a::attr(href)").get()
            if next_page is not None:
                logging.info("next_page is :"+next_page)
                yield response.follow(next_page, self.parse_content)

        logging.info("Append done.")

    # 抽取每个页面的标题和内容
    def parse_content(self, response):
        # yield {
        #     'name:': response.css("div.bookname h1::text").get(),
        #     'content:': response.css("div#content::text").getall(),
        # }
        item = NovelItem()
        item['name'] = response.css("div.bookname h1::text").get()
        item['content'] = response.css("div#content::text").getall()
        yield item
