import scrapy


class BaiduSpider(scrapy.Spider):

    # name是爬虫的名称
    name = "baidu"

    # 起始url列表
    start_urls = ['http://www.baidu.com']

    # 负责分析dowmloader下载得到的结果
    # 重写parse
    def parse(self, response):
        '''
        只是保存网页即可
        :param response:
        :return:
        '''
        with open('baidu.html', 'w', encoding='utf-8') as f:
            f.write(response.body.decode('utf-8'))