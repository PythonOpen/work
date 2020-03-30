'''
利用selenium模拟登录豆瓣
需要输入验证码
思路：
1. 保存页面成快照
2. 等待用户手动输入验证码
3. 继续自动执行提交等动作

'''

from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
import time

url = 'https://accounts.douban.com/login?alias=&redir=https%3A%2F%2Fwww.douban.com%2F&source=index_nav&error=1001'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
executable_path = "D:\chrome\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options, executable_path=executable_path)
driver.get(url)

time.sleep(4)

# 生成快照，用来查看验证码
driver.save_screenshot('douban_index.png')

# captcha = input("plz input youre code:")

# 利用账户信息和验证码登录
driver.find_element_by_xpath("//li[@class='account-tab-account']").click()
driver.find_element_by_id("username").send_keys("1366798119@qq.com")
driver.find_element_by_id("password").send_keys("haha123456")
# driver.find_element_by_id("captcha_field").send_keys(captcha)

driver.find_element_by_xpath("//div[@class='account-form-field-submit ']/a").click()

time.sleep(5)

driver.save_screenshot("logined.png")

captcha = input("plz input youre code:")

with open("douban_home.html", 'w', encoding='utf-8') as file:
    file.write(driver.page_source)


driver.quit()
