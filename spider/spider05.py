import requests
import re
'''
利用正则来爬去猫眼电影
1. url: http://maoyan.com/board
2. 把电影信息尽可能多的拿下来

分析
1. 一个影片的内容是以dd开是的单元
2. 在单元内存在一部电影的所有信息

思路：
1. 利用re把dd内容都给找到
2. 对应找到的每一个dd，用re挨个查找需要的信息

方法就是三步走：
1. 把页面down下来
2. 提取出dd单元为单位的内容
3. 对每一个dd，进行单独信息提取
'''

# 1 下载页面内容
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
}
url = "https://maoyan.com/board"

# req = request.Request(url, headers=headers)
rsp = requests.get(url, headers=headers)
html = rsp.text
# rsp = request.urlopen(req)
# html = rsp.read().decode()

# print(html)

# '.'匹配所有除\n,\r的任何字符
s = r'<dd>(.*?)</dd>'

# re.S表示匹配包括整个字符串包括
pattern = re.compile(s, re.S)

films = pattern.findall(html)
print(len(films))

for film in films:
    s = r'<div.*?title="(.*?)"'
    pattern = re.compile(s, re.S)
    title = pattern.findall(film)[0]
    print(title)
