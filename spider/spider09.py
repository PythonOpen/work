'''
https://book.douban.com/subject_search?search_text=python&cat=1001&start=%s0
使用selenium爬取页面
保存内容后用xpath进行分析
'''

from selenium import webdriver
import time
from lxml import etree


def get_web(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    executable_path = "D:\chrome\chromedriver\chromedriver.exe"
    driver = webdriver.Chrome(options=chrome_options, executable_path=executable_path)
    driver.get(url)

    print('waitting for .......')
    time.sleep(20)
    print('waitting done .......')

    driver.save_screenshot('douban_reader.png')


    fn = 'douban_reader.html'
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(driver.page_source)

    content_parse(fn)
    driver.quit()

def content_parse(fn):
    html = ''

    with open(fn, 'r', encoding='utf-8') as f:
        html = f.read()

    # 生成xml树
    tree = etree.HTML(html)

    #查找book
    books = tree.xpath('//div[@class="item-root"]')

    for book in books:
        book_name = book.xpath(".//div[@class='title']/a")
        print(book_name[0].text)


if __name__ == '__main__':
    url = 'https://search.51job.com/list/030200,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    get_web(url)




















