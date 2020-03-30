from urllib import request, response, parse
# method get
'''
http://www.langlang2017.com/index.html
http://www.langlang2017.com/route.html
http://www.langlang2017.com/FAQ.html
'''


def spider(url):
    user_agent_list = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    ]
    headers = {
        'user-agent': user_agent_list[0],

    }
    req = request.Request(url=url, headers=headers)
    resp =request.urlopen(req)

    html = resp.read().decode()
    # print(html)
    name = url.split('/')
    fileName = 'Tl'+name[-1]
    # print(name)
    with open(fileName, 'w', encoding='utf-8')as f:
        f.write(html)


if __name__ == "__main__":
    url_list = [
        'http://www.langlang2017.com/index.html',
        'http://www.langlang2017.com/route.html',
        'http://www.langlang2017.com/FAQ.html'
    ]
    for url in url_list:
        spider(url)
