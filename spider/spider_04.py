from urllib import request, response, parse
# method get
'''
https://tieba.baidu.com/f?kw=%E9%87%91%E5%BA%B8&ie=utf-8&pn=0
https://tieba.baidu.com/f?kw=金庸&ie=utf-8&pn=100
'''

url = "https://tieba.baidu.com/f?"
name = input("请输入贴吧名称:")
page = input("请输入贴吧页数:")
# print(type(page))
for i in range(int(page)):
    qs = {
        'kw': name,
        'ie': 'utf-8',
        'pn': str(page*50)
    }
    qs_data = parse.urlencode(qs)
    url = url + qs_data

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',

    }

    req = request.Request(url=url, headers=headers)
    resp = request.urlopen(req)

    html = resp.read().decode()
    with open(name+'第'+str(i+1)+'页'+'html', 'w', encoding='utf-8')as f:
        f.write(html)

