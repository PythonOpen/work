import requests
from lxml import etree
import os
import time


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'referer': 'https://www.aitaotu.com/zxtp/etfxgt'
}


def mz_spider(base_url):
    global headers
    res = requests.get(base_url, headers=headers)
    html = etree.HTML(res.text)
    time.sleep(1)
    # 获取详情页信息
    # print(res.text)
    with open('meizitu.html', 'wb')as f:
        f.write(res.content)
    img_src = html.xpath('//div[@class="item masonry_brick"]/div[@class="item_t"]/div[@class="img"]/a/@href')
    print(len(img_src))
    for img_url in img_src:
        img_url = 'https://www.aitaotu.com' + img_url
        img_parse(img_url)


def img_parse(img_url):
    global headers
    res = requests.get(img_url, headers=headers)
    html = etree.HTML(res.text)
    time.sleep(1)
    # 获取标题
    title = html.xpath('//div[@class="wrapper clearfix imgtitle sut6552"]/h1/text()')[0]
    print(title)
    # 获取图片总的页面数
    page_num = html.xpath('//div[@class="pages"]/ul/li/a/text()')[-3]
    print(page_num)

    # 拼接图片详情页地址
    for num in range(1, int(page_num)+1):
        if num == 1:
            img_src = img_url
        else:
            img_src = img_url.split('.html')[-2]+'_'+str(num)+'.html'
        print(img_src)
        download_img(img_src, title)


# 下载图片
def download_img(img_src, title):
    global headers
    res = requests.get(img_src, headers=headers)
    html = etree.HTML(res.text)
    # 获取图片的具体连接地址
    img_url = html.xpath('//div[@class="big-pic"]/div[@id="big-pic"]/p/a/img/@src')[0]

    # 下载路径
    root_dir = 'mzi_img'
    img_url_list = img_url.split('/')
    img_name = img_url_list[-1]
    print(img_name)
    title = title.replace(' ', '')
    title = title.replace('?', '')
    root_dir = root_dir+"\\" + title
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)
    # path = '/' + img_url_list[-3] + '/' + img_url_list[-2] + '/' + img_url_list[-1]
    # 模拟消息头
    header = {
        'referer': img_src,
        'user-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    }
    res = requests.get(img_url, headers=header)
    time.sleep(1)
    with open(root_dir+"\\"+img_name, 'wb')as f:
        f.write(res.content)
        f.close()
        print(title+"~"+img_name+"文件保存成功~~")


if __name__ == "__main__":
    # https://www.mzitu.com/page/6/
    for i in range(1, 2):
        if i == 1:
            base_url = "https://www.aitaotu.com/zxtp/etfxgt"
            # base_url = "https://www.mzitu.com"
        else:
            # base_url = "https://www.mzitu.com/page/{}/".format(str(i))
            base_url = "https://www.aitaotu.com/zxtp/etfxgt/list_{}.html".format(str(i))
        time.sleep(1)
        mz_spider(base_url)
