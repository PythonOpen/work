from urllib import request
import random

isProxy = input("please input is proxy? y/n:")

# 有代理
proxy_1 = request.ProxyHandler({"http": "171.12.112.49:9999"})

# 无代理
proxy_2 = request.ProxyHandler()

opener = request.build_opener(proxy_2)

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
}

if isProxy == 'y':
    opener = request.build_opener(proxy_1)

url = "https://www.baidu.com"

req = request.Request(url, headers=headers)

response = opener.open(req)

content = response.read().decode()

print(content)
