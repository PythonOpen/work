import requests
from lxml import etree
import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import win32api
import win32con

VK_CODE = {'enter': 0x0D, 'down_arrow': 0x28}
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('disable-infobars')
prefs = {
    # "profile.managed_default_cont
    # ent_settings.images": 2,
    "download.default_directory": r"F:\\Download",
    # "download.prompt_for_download": False
}
chrome_options.add_experimental_option('prefs', prefs)
executable_path = "D:\chrome\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=executable_path)

# 键盘键按下
def keyDown(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, 0, 0)


# 键盘键抬起
def keyUp(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)


def mz_spider(base_url, driver):
    driver.get(base_url)
    html = etree.HTML(driver.page_source)
    # 获取详情页信息
    img_src = html.xpath('//div[@class="postlist"]/ul/li/a/@href')
    for img_url in img_src:
        img_parse(img_url, driver)
    driver.quit()


def img_parse(img_url, driver):
    driver.get(img_url)
    html = etree.HTML(driver.page_source)
    # 获取标题
    title = html.xpath('//div[@class="content"]/h2/text()')[0]
    print(title)
    # 获取图片总的页面
    page_num = html.xpath('//div[@class="pagenavi"]/a/span/text()')[-2]
    print(page_num)
    root_dir = 'mz_img'
    title = title.replace(' ', '')
    root_dir = root_dir + "\\" + title
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)
    root_dir = root_dir + "\\" + title
    prefs = {'profile.default_content_settings.popups': 0,
             "download.default_directory": '.'}
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('disable-infobars')
    # executable_path = "D:\chrome\chromedriver\chromedriver.exe"
    # driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=executable_path)
    # driver.maximize_window()
    # driver.implicitly_wait(10)
    time.sleep(1)

    # 拼接图片详情页地址
    for num in range(1, int(page_num)+1):
        if num == 1:
            img_src = img_url
        else:
            img_src = img_url+"/"+str(num)
        print(img_src)
        download_img(img_src, driver)


# 下载图片
def download_img(img_src, driver):
    driver.get(img_src)
    # html = etree.HTML(driver.page_source)
    #
    # # 获取图片的具体连接地址
    # img_url = html.xpath('//div[@class="main-image"]/p/a/img/@src')[0]
    #
    # # 下载路径
    # root_dir = 'mz_img'
    # img_name = img_url.split('/')[-1]
    # print(img_name)
    # title = title.replace(' ', '')
    # root_dir = root_dir+"\\" + title
    # if not os.path.exists(root_dir):
    #     os.makedirs(root_dir)
    element = driver.find_elements_by_xpath('//div[@class="main-image"]/p/a/img')[0]
    img_url = element.get_attribute('src')
    img_desc = element.get_attribute('data-desc')
    action = ActionChains(driver).move_to_element(element)
    action.context_click(element).perform()
    time.sleep(2)
    # 按v
    win32api.keybd_event(86, 0, 0, 0)
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(1)
    # 按enterv
    keyDown("enter")
    keyUp("enter")
    # action.send_keys(Keys.ARROW_DOWN)
    # action.send_keys('v')
    # action.perform()
    time.sleep(1)
    # with open(root_dir+"\\"+img_name, 'wb')as f:
    #     f.write(res.content)
    #     f.close()
    #     print(title+"~"+img_name+"文件保存成功~~")


if __name__ == "__main__":
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    #     'referer': 'https://www.mzitu.com'
    # }
    # https://www.mzitu.com/page/6/
    for i in range(1, 2):
        if i == 1:
            base_url = "https://www.mzitu.com"
        else:
            base_url = "https://www.mzitu.com/page/{}/".format(str(i))
        time.sleep(1)
        mz_spider(base_url, driver)
