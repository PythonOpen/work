import requests
import csv
from lxml import etree
import json
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

r = requests.get('http://www.seputu.com/', headers=headers)

html = etree.HTML(r.text)
div_mulus = html.xpath('//*[@class="mulu"]')

content = []
for div_mulu in div_mulus:
    # 标题
    div_h2 = div_mulu.xpath('.//div[@class="mulu-title"]/center/h2/text()')
    if len(div_h2) > 0:
        # print(h2.string)
        h2_title = div_h2[0]
        a_s = div_mulu.xpath('./div[@class="box"]/ul/li/a')
        list = []
        # 获取章节内容与url地址
        for a in a_s:
            # print(a)
            href = a.xpath('./@href')[0]
            box_title = a.xpath('./@title')[0]
            pattern = re.compile(r'\s*\[(.*)\]\s+(.*)')
            match = pattern.search(box_title)
            # box_title = a.contents
            print(href, box_title, match)
            
#             list.append({'href': href, 'box_title': box_title})
#         content.append({'title': h2_title, 'content': list})
#
# with open('dmbj.json', 'w', encoding='utf-8') as fp:
#     json.dump(content, fp=fp, indent=4, ensure_ascii=False)
