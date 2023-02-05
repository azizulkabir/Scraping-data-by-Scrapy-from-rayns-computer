import scrapy


class LaptopSpider(scrapy.Spider):
    name = "laptop"

    start_urls = [
        "https://www.ryanscomputers.com/category/laptop-all-laptop?osp=0"]

    def parse(self, responses):
        response = responses.xpath('//div[@class="card-body text-center"]')
        for i in response:
            title = i.xpath(
                '//p[@class="card-text p-0 m-0 grid-view-text"]/a/text()').get()

            yield {
                'title': title,
               
            }
