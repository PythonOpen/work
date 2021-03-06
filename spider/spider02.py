
'''
构建代理集群/队列
每次访问服务器，随机抽取一个代理
抽取可以使用 random.choice

分析步骤：
1. 构建代理群
2. 每次访问，随机选取代理并执行
'''


from urllib import request, error
import random

# 使用代理步骤
# 1. 设置代理地址
proxy_handler_list = []
proxy_list = [
    # 列表中存放的是dict类型的元素
    {"http": "39.137.69.8:8080"},
    {"http": "60.167.103.208:9999"},
    {"http": "101.95.115.196:8080"},
    {"http": "36.27.28.67:9999"}
]

for proxy in proxy_list:
    proxy_handler = request.ProxyHandler(proxy)
    proxy_handler_list.append(proxy_handler)

opener_list =[]
for proxy_handler in proxy_handler_list:
    opener = request.build_opener(proxy_handler)
    opener_list.append(opener)

url = "http://www.baidu.com"
try:
    opener = random.choice(opener_list)
    request.install_opener(opener)
    rsp = request.urlopen(url)
    html = rsp.read().decode()
    print(html)
except error.URLError as e:
    print(e)
except Exception as e:
    print(e)


# def a(func, d, c, x, y):
#     func(x, y)
#     d(x, y)
#     c(x, y)
#
#
# def k(x, y):
#     print("func", x, y)


# if __name__ == '__main__':
#     a(k, k, k, 'a', 'b')



