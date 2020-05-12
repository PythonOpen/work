- 爬虫项目大概流程
    - 新建项目：scrapy startproject xxx
    - 明确需要目标/产出：编写item.py
    - 制作爬虫：地址spider/xxspider.py
    - 储存内容: pipelines.py
    
- 案例 e14-scrapy-baidu
- 利用最简单的爬虫
- 爬取百度页面
- 关闭配置机器人协议
    
- 案例 e15-meiju
- 创建新项目
- 分析网页，定义item
- 编写pipeline, 确定如何处理item
- 编写spider,确定如何提取item
- 可以通过增加一个单独命令文件的方式在pycharm中启动爬取

- 案例scrapy03 qq招聘
- 创建项目
- 编写item
- 编写spider
- 编写pipeline
- 设置pipeline

- 案例scrapy04 校花网 
- 创建项目
- 编写item
- 编写spider
- 编写pipeline
- 设置pipeline
- 中间件，会使用selenium
- settings设置

# 验证码问题
    - 验证码：防止机器人或者爬虫
    - 分类:
        - 简单图片
        - 极验，官网www.geetest.com
        - 12306
        - 电话
        - google验证
        
    - 验证码破解
        - 通用方法：
            - 下载网页和验证码
            - 手动输入验证号码
        - 简单图片
            - 使用图像识别软件或者文字识别软件
            - 可以使用第三方图像验证码破解网站
        - 极验，官网www.geetest.com
            - 破解比较麻烦
            - 可以模拟鼠标等移动
            - 一直在进化
        - 12306
        - 电话：语音识别
        - google验证    

# Tesseract
- 集齐视觉领域的基础软件
- OCR:OpticalChracterRecognition,光学文字识别
- Tesseract：一个ocr库，有google赞助
- 安装:
    - windows:https://jingyan.baidu.com/article/219f4bf788addfde442d38fe.html
    - 安装完后需要设置虚拟环境
- 安装完后还需要pytesseract
    - pip install pytesseract
    
# 分布式
1.什么是分布式
    - 所谓的分布式就是指将一个大的数据拆分成若干个小的部分，分别交给不同的
    计算机节点去操作，最终在将计算结果进行汇总
2. 分布式爬虫能做什么事情
    - 集群式工作
    - 提高效率
    - 突破带宽的限制
    
# redis
- 内存型数据库
- 以keys-values存放数据
    - 解决：
    - 1.队列问题
    - 2.过滤问题（url地址过滤）(集合)
    - 3.数据存储问题
- 缺点
   - 维护成本高
   - 硬件成本高
   - 人力成本较高
