from urllib import request, parse


url = "http://www.baidu.com"
resp = request.urlopen(url)
print(resp)
content = resp.read().decode('utf-8')
print(content)

