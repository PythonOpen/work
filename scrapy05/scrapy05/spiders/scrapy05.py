from scrapy05.items import QQItem
import re
import scrapy


# 用来定义spider
class QQSpider(scrapy.Spider):

    name = "QQ"
    # allowed_domains为允许访问的域名信息
    allowed_domains = ['search.51job.com']
    start_urls = ['https://search.51job.com/list/030200,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']

    # 重写parse
    # 下载结果自动放在response内存储
    def parse(self, response):
        trs1 = response.xpath('//a[@onmousedown=""]')
        trs2 = response.xpath('//div[@class="el"]/span[@class="t2"]')
        trs3 = response.xpath('//div[@class="el"]/span[@class="t3"]')
        trs4 = response.xpath('//div[@class="el"]/span[@class="t4"]')
        trs5 = response.xpath('//div[@class="el"]/span[@class="t5"]')

        print(len(trs1))
        print(len(trs2))
        print(len(trs3))
        print(len(trs4))
        print(len(trs5))

        for trs1s, trs2s, trs3s, trs4s, trs5s in zip(trs1, trs2, trs3, trs4, trs5):
            item = QQItem()
            item['name'] = trs1s.xpath('./text()').extract()[0]
            item['company'] = trs2s.xpath('./a/@title').extract()[0]
            item['href'] = trs2s.xpath('./a/@href').extract()[0]
            item['location'] = trs3s.xpath('./text()').extract()[0]
            item['salary'] = trs4s.xpath('./text()').extract()
            item['date'] = trs5s.xpath('./text()').extract()[0]

            # 处理继续爬取的链接
            # 通过得到当前页，提取数字，把数据加1，替换原来的数字，就是下一个页面信息
            curpage = re.search('(\d+)\.html\?', response.url).group(0)
            curpage = re.search('(\d+)', curpage).group(0)
            page = str(int(curpage)+1)+'.html?'
            # 生成下一个url
            url = re.sub('(\d+)\.html\?', str(page), response.url)
            # 注意callback的写法
            yield scrapy.Request(url, callback=self.parse)

            # 将获取的item提交给pipeline
            yield item
            # 把地址通过yield返回

