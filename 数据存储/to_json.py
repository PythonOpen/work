# import json
# """
# python对json文件操作分为编码与解码
# dumps 字符串
# dump json对象 可以通过fp文件流写入文件
# 解码:
#     load
#     loads
# """
#
# str = "[{'username': '大拿', 'age': '18'}]"
#
# json_str = json.dumps(str, ensure_ascii=False)
# print(json_str)
# print(type(json_str))
# new_str = json.loads(json_str)
# print(new_str, type(new_str))

import requests,json
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
r = requests.get('http://www.seputu.com/', headers=headers)
print(r.text)

soup = BeautifulSoup(r.text, 'lxml')
content = []
for mulu in soup.find_all(class_='mulu'):
    # 标题
    h2 = mulu.find('h2')
    if h2 is not None:
        # print(h2.string)
        h2_title = h2.text
        list = []
        # 获取章节内容与url地址
        for a in mulu.find(class_="box").find_all('a'):
            # print(a)
            href = a.get('href')
            box_title = a.get('title')
            # box_title = a.contents
            print(href, box_title)
            list.append({'href': href, 'box_title': box_title})
        content.append({'title': h2_title, 'content': list})

with open('dmbj.json', 'w', encoding='utf-8') as fp:
    json.dump(content, fp=fp, indent=4, ensure_ascii=False)
