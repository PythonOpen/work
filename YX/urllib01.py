"""
https://tieba.baidu.com/f?kw=%E9%87%91%E5%BA%B8&ie=utf-8&pn=0&pagelets=frs-list%2Fpagelet%2Fthread&pagelets_stamp=1588914207273
"""
from urllib import request, parse

url = "https://tieba.baidu.com/f?"
name = input("请输贴吧的名称:")
page = input("请输入贴吧页数:")
for i in range(int(page)):
    qs = {
        'kw': name,
        'ie': 'utf-8',
        'pn': i*50,
    }
    qs_data = parse.urlencode(qs)
    url = url + qs_data
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    }
    req = request.Request(url, headers=headers)
    response = request.urlopen(req)

    html = response.read().decode()
    with open(name+"第"+str(i+1)+"页"+".html", 'w', encoding='utf-8') as f:
        f.write(html)
