import scrapy

#导入需要的item
from scrapy02.items import MeijuItem


# 用来定义spider
class MeijuSpider(scrapy.Spider):

    name = "meiju"
    start_urls = ['https://www.meijutt.tv/new100.html']

    # 重写parse
    def parse(self, response):
        '''
        默认已经得到了网页
        反馈内容需要用response表示
        其中包括需要的所有数据
        :param response:
        :return:
        '''
        movies = response.xpath('//h5/a[@href]')
        states = response.xpath('//span[@class="state1 new100state1"]/font[@color]')
        tvs = response.xpath('//span[@class="mjtv"]')
        times = response.xpath('//div[@class="lasted-time new100time fn-right"]')
        i = 0

        for movie, state, tv, time in zip(movies, states , tvs, times):
            '''
            每个movie都需要换成一个item
            '''
            # movie.xpath('./@title').extract()[0] —— extract()为构造器，提取含有属性title的值列表返回。
            i += 1
            item = MeijuItem()
            item['name'] = movie.xpath('./@title').extract()[0]
            item['href'] = movie.xpath('./@href').extract()[0]
            item['state'] = state.xpath('./text()').extract()[0]
            tv = tv.xpath('./text()')
            if len(tv):
                item['tv'] = tv.extract()[0]
            else:
                item['tv'] = ""
            if i == 1 or i == 2:
                item['time'] = time.xpath('./font/text()').extract()[0]
            else:
                item['time'] = time.xpath('./text()').extract()[0]
            # 处理继续爬取的链接
            # 通过得到当前页，提取数字，把数字加10，替换原来的数字，就是下一页的地址
            yield item

