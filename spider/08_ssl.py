from urllib import request
import ssl

# ssl免认证
ssl._create_default_https_context = ssl._create_unverified_context

base_url = "http://www.12306.cn/mormhweb/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
}
req = request.Request(url=base_url, headers=headers)
response = request.urlopen(req)
html = response.read().decode()
print(html)


