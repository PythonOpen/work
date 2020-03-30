from urllib import request
# import ssl
from lxml import etree

# ssl免认证
# ssl._create_default_https_context = ssl._create_unverified_context

base_url = "http://zuihaodaxue.com/zuihaodaxuepaiming2019.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
}
req = request.Request(url=base_url, headers=headers)
response = request.urlopen(req)
html = response.read().decode()

html = etree.HTML(html)

items = html.xpath('//tr[@class="alt"]')
# print(items)

for item in items:
    # 排名
    number = item.xpath('./td')[0].text
    # 大学
    school = item.xpath('.//div[@align="left"]')[0].text
    # 省份
    addr = item.xpath('./td')[2].text
    # 总分
    score = item.xpath('./td')[3].text
    print(number+"..."+school+"..."+addr+"..."+score+"...")


