import scrapy


class LaptopSpider(scrapy.Spider):
    name = "laptop"
    allowed_domains = ["www.ryanscomputers.com"]
    start_urls = ["http://www.ryanscomputers.com/"]

    def parse(self, response):
        pass
