'''
任务：
1. 通过selenium模拟对页面元素的控制

'''
from selenium import webdriver
import time

url = 'https://www.baidu.com'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
executable_path = "D:\chrome\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options, executable_path=executable_path)
driver.get(url)

# 通过js来控制网页内容
# 需要先把js编写出来
# 然后通过execute_script 执行

# 美化输入框，输入框id是kw
js = "var q=document.getElementById(\'kw\'); q.style.border=\'2px solid red\';"

# 执行代码
driver.execute_script(js)

time.sleep(3)
driver.save_screenshot('redbaidu.png')

# js隐藏相应元素，我们这里隐藏logo
img = driver.find_element_by_xpath('//*[@id="lg"]/img')
driver.execute_script('$(arguments[0]).fadeOut()', img)

# 滚动滑动条到最底下
js = "$('.scroll_top').click( function(){$('html, body').animate({scrollTop: '0px'}, 800)} );"
driver.execute_script(js)

# 查看网页快照
time.sleep(3)
driver.save_screenshot("nullbaidu.png")

