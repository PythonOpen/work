import scrapy
from urllib import request

from scrapy04.items import XiaohuaItem


class XiaohuaSpider(scrapy.Spider):

    name = 'xiaohua'
    allowed_domains = ['nice.ruyile.com']

    start_urls = ['https://nice.ruyile.com/?f=5']

    def parse(self, response):
        bookmarks = response.xpath('//div[@class="tp_list"]')

        for bm in bookmarks:
            item = XiaohuaItem()
            item['title'] = bm.xpath('./div[@class="tp_mz"]/a/text()').extract()[0]
            href = bm.xpath('./div[@class="tp_a"]/a/@href').extract()[0]
            item['src'] = bm.xpath('./div[@class="tp_a"]/a/img/@src').extract()[0]
            # 拼接网址
            item['href'] = request.urljoin(response.url, href)

            yield item


