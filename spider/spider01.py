from urllib import request, parse


def add(**data):
    print(data)


if __name__ == "__main__":
    qs = {
        "kw": "张继科",
        "ie": "utf-8",
        "pn": 0
    }

    urls = []
    baseurl = "https://tieba.baidu.com/f?"
    for i in range(10):
        pn = i*50
        qs['pn'] = str(pn)
        urls.append(baseurl + parse.urlencode(qs))

    print(urls)
    for url in urls:
        rsp = request.urlopen(url)
        html = rsp.read().decode("utf-8")
        print(url)
        # 'a'表示可往文件追加内容
        with open('spider.html', 'a', encoding='utf-8')as f:
            f.write(html+"\n"+"="*20)

    # add(data={'a': 1, 'b': 4, 'c': 5})
    #
    # add(city='beijing', age=10)

