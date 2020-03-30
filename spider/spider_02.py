from urllib import request, response, parse
# method get

url = "https://www.w3school.com.cn/json/index.asp"
resp = request.urlopen(url)
print(resp)
content = resp.read().decode('gb2312', "ignore")
print(content)

