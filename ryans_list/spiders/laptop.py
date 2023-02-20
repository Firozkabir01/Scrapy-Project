import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class LaptopSpider(CrawlSpider):
    name = "laptop"
    # allowed_domains = ["ryanscomputer.com"]
    start_urls = [
        "https://www.ryanscomputers.com/category/laptop-all-laptop?limit=100&osp=0"
        ]

    rules = (Rule(LinkExtractor(restrict_xpaths='//p[@class="card-text p-0 m-0 list-view-text"]/a'),
                  callback="parse_item", follow=True),
            Rule(LinkExtractor(restrict_xpaths='//a[@aria-label="Next »"]'), follow=True),
                  )

    def parse_item(self, response):

        yield {
            'title': response.xpath('//div[@class="product_content h-100"]/h1/text()').get().strip(),
            'price(tk)': response.xpath('(//span[@class="rp-block mb-2"]/span)[1]/text()').get().replace('Regular Price Tk ',''),
            'special_price(tk)': response.xpath('//span[@class="sp-block"]/text()').get().replace('Special Price Tk ', ''),
            'emi': response.xpath('//span[@class="rp-block mb-2"]/a/text()').get().strip(),
            'reviews': response.xpath('//a[@class="review-link"]/text()').get(),
            'product_id': response.xpath('//div[@class="product_content h-100"]/p/span/text()').get(),
            'ram': response.xpath('//li[contains(text(), "RAM")]/text()').get().replace('RAM - ', ''),
            'storage': response.xpath('//li[contains(text(), "Storage")]/text()').get().replace('Storage - ', ''),
            'generation': response.xpath('//li[contains(text(), "Generation")]/text()').get().replace('Generation - ', ''),
            'graphics_memory': response.xpath('//li[contains(text(), "Graphics Memory")]/text()').get().replace('Graphics Memory - ', ''),
            'processor_type': response.xpath('//li[contains(text(), "Processor Type")]/text()').get().replace('Processor Type. - ', ''),
            'display_size(inch)': response.xpath('//li[contains(text(), "Display Size")]/text()').get().replace('Display Size (Inch) - ', '')
        }
