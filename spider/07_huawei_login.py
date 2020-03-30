from urllib import request, parse
from http import cookiejar

'''
urllib模拟登录华为官网
url='https://www.huawei.com/en/accounts/LoginPost'
method:post
parm:
    userName:1541623372@qq.com
    pwd:Guc1XJUv42hpoPoYsqjbMRoAlp6W+2yGvxfu/KwbotCZsYHKVd3FOBg9sj0qTkSdBhn++9+N90S31m1PbyOOJa2nT3vvq7ATiLjKF8oGbS7uGF9XHGmQqf730B/IEKmlejU4u9qMgvRuWmueNMxqvJkMxqYkBJktUs1IT0PwIGk=
    languages:zh
    fromsite:www.huawei.com
    authMethod:password
'''
# 生成cookie对象
cookie = cookiejar.CookieJar()
# 生成cookie管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 生成http请求管理器
http_handler = request.HTTPHandler()
# 生成https请求管理器
https_handler = request.HTTPSHandler()

# 构建发起请求管理器
opener = request.build_opener(cookie_handler,http_handler,https_handler)

# 构建登录函数


def login(url):
    data = {
        "userName": "yuxiang000",
        "pwd": "Huawei12#$",
        "languages": "zh",
        "fromsite": "www.huawei.com",
        "authMethod": "password"
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    }

    data = parse.urlencode(data)
    # data的数据类型为bytes
    req = request.Request(url, data=bytes(data,"utf-8"), headers=headers)
    content = opener.open(req)
    content = content.read().decode('utf-8')
    print(content)


if __name__ == "__main__":
    url = 'https://www.huawei.com/en/accounts/LoginPost'
    login(url)

