'''
爬取腾讯招聘的网站 https://hr.tencent.com/position.php?&start=10#a
'''

from bs4 import BeautifulSoup
from urllib import request


def qq():
    # 获取页面
    url = 'https://search.51job.com/list/030200,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    rsp = request.urlopen(url)
    html = rsp.read()

    # 提取数据
    # 用bs解析
    soup = BeautifulSoup(html, 'lxml')

    # 创建css选择器，得到相应的tags
    trs1 = soup.select('p[class="t1"]')
    trs2 = soup.select('div[class="el"] span[class="t2"]')
    trs3 = soup.select('div[class="el"] span[class="t3"]')
    trs4 = soup.select('div[class="el"] span[class="t4"]')
    trs5 = soup.select('div[class="el"] span[class="t5"]')

    # trs0 = []
    # trs = []
    # for i in range(len(trs1)):
    #     trs0.append(trs1[i])
    #     trs0.append(trs2[i])
    #     trs0.append(trs3[i])
    #     trs0.append(trs4[i])
    #     trs0.append(trs5[i])
    #     trs.append(trs0)
    #     trs0 = []
    #
    # for tr in trs:
    #     name = tr[0].select('a')[0].get_text()
    #     print(name)
    #     company = tr[1].select('span > a')[0].attrs['title']
    #     print(company)
    #     href = tr[1].select('span > a')[0].attrs['href']
    #     print(href)
    #     location = tr[2].get_text()
    #     print(location)
    #     salary = tr[3].get_text()
    #     print(salary)
    #     date = tr[4].get_text()
    #     print(date)
    #     print("==" * 12)

    for trs1s, trs2s, trs3s, trs4s, trs5s in zip(trs1, trs2, trs3, trs4, trs5):
        name = trs1s.select('a')[0].get_text()
        print(name)
        company = trs2s.select('span > a')[0].attrs['title']
        print(company)
        href = trs2s.select('span > a')[0].attrs['href']
        print(href)
        location = trs3s.get_text()
        print(location)
        salary = trs4s.get_text()
        print(salary)
        date = trs5s.get_text()
        print(date)
        print("==" * 12)


if __name__ == '__main__':
    qq()
