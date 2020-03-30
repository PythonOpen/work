''''
任务：
1. 利用selenium模拟鼠标下拉
2. 每次多出现几部电影的信息
'''

from selenium import webdriver
import time

url = 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action='

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
executable_path = "D:\chrome\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options, executable_path=executable_path)
driver.get(url)


# 向下滚动10000像素
js = 'document.documentElement.scrollTop=10000'
time.sleep(3)


driver.save_screenshot('douban1.png')

driver.execute_script(js)
time.sleep(3)


driver.save_screenshot('douban2.png')
driver.quit()
