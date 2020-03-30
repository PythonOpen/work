from urllib import request
import random

# 代理
proxy_list = [
    {"http": "171.12.112.49:9999"},
    {"http": "112.84.99.144:9999"},
    {"http": "163.204.246.142:9999"}
]

proxy = random.choice(proxy_list)

# 构造代理管理器
proxy_hander = request.ProxyHandler(proxy)

#创建网络请求对象opener
opener = request.build_opener(proxy_hander)

url = "https://www.baidu.com/"

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
}

req = request.Request(url, headers=headers)

response = opener.open(req)

content = response.read().decode()

print(content)

