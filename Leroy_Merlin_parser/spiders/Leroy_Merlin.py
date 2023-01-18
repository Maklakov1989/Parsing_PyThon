import scrapy
from scrapy.http import HtmlResponse
from Leroy_Merlin_parser.items import AdsParserItem
from scrapy.loader import ItemLoader


class LeroyMerlinSpider(scrapy.Spider):
    name = 'Leroy_Merlin'
    allowed_domains = ['leroymerlin.ru']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f'https://leroymerlin.ru/search/?q={kwargs.get("search")}/']


    def parse(self, response):
        links = response.xpath("//div[@class='phytpj4_plp largeCard']/a")
        for link in links:
            yield response.follow(link, callback=self.parse_Leroy_Merlin)

    def parse_ads(self, response: HtmlResponse):
        loader = ItemLoader(item=AdsParserItem(), response=response)

        loader.add_xpath('name', "//h1/text()")
        loader.add_xpath('price', "//span[@slot= 'price']//text()")
        #loader.add_xpath('photos', "//div[@class='swiper-zoom-container']/img/@src | //div[@class='swiper-zoom-container']/img/@data-src")
        #loader.add_value('url', response.url)
        yield loader.load_item()
