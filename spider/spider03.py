from urllib import request, parse
from http import cookiejar
import ssl

'''
登录开心网
利用cookie
免除ssl
'''
# 忽略安全问题
ssl._create_default_https_context = ssl._create_unverified_context
cookie = cookiejar.CookieJar()
cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()

opener = request.build_opener(http_handler, https_handler, cookie_handler)

'''
步骤：
1， 寻找登录入口， 通过搜查相应文字可以快速定位
  login_url = "https://security.kaixin001.com/login/login_post.php"
  相应的用户名和密码对应名称为email, password
2. 构造opener
3. 构造login函数
'''
# long_url = "https://security.kaixin001.com/login/login_post.php"


def login():
    long_url = "https://security.kaixin001.com/login/login_post.php"
    data = {
        "email": "13119144223",
        "password": "123456"
    }
    data = parse.urlencode(data)
    # data要求是一个bytes对象，所以需要进行编码
    headers = {
        "Context-Length": len(data),
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    }
    req = request.Request(long_url, data=data.encode(), headers=headers)
    rsp = opener.open(req)
    html = rsp.read()
    html = html.decode()
    print(html)


def getHomePage():
    base_url = "http://www.kaixin001.com/home/?_profileuid=181697221"
    # 自动输入cookie
    rsp = opener.open(base_url)
    html = rsp.read()
    html = html.decode()

    print(html)


if __name__ == '__main__':
    login()
    getHomePage()


