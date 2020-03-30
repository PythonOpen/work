from urllib import request, parse
import json

def db_spider(content):
    # 参数分段
    data = {
        'kw': content
    }

    # 参数的拼接封装转码
    data = parse.urlencode(data)

    # 请求地址
    base_url = "https://fanyi.baidu.com/sug"

    # 封装headers头部信息
    headers = {
        'Content-Length': len(data),
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    }

    # 封装Request对象
    req = request.Request(url=base_url, data=bytes(data, encoding='utf-8'), headers=headers)
    response = request.urlopen(req)
    html = response.read().decode()

    # print(html)
    # 使用json格式化数据
    json_data = json.loads(html)
    print(json_data)
    for item in json_data['data']:
        print(item['k'], item['v'])


if __name__ == "__main__":
    content = input('请输入您要翻译的内容:')
    db_spider(content)
