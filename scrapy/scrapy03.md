# scrapy
# 爬虫框架
- 框架
- 爬虫框架
    - scrapy
    - pyspider
    - crawley
- scrapy框架介绍
    - https://doc.scrapy.org/en/latest/
    - http://scrapy-chs.readthedocs.io/zh_cn/latest/index.html
- 安装
    - 利用pip
    
- scrapy概述
    - 包含各个部件
        - ScrapyEngine: 神经中枢，大脑，核心
        - Scheduler调度器： 引擎发来的request请求，调度器需要处理，然后交换引擎
        - Downloader下载器：把引擎发来的requests发出请求，得到response
        - Spider爬虫：负责把下载器得到的网页/结果进行分解，分解成数据+链接
        - ItemPipeline管道：详细处理Item
        - DownloaderMiddleware下载中间件：自定义下载的功能扩展组件
        - SpiderMiddleware爬虫中间件：对spider进行功能扩展
    - 爬虫项目大概流程
        - 新建项目：scrapy startproject xxx
        - 明确需要目标/产出：编写item.py
        - 制作爬虫：地址spider/xxspider.py
        - 存储内容：pipelines.py
    - ItemPipeline
        - 对应的是pipeline文件
        - 爬虫提取出数据存入item后，item中保存的数据需要进一步处理，比如清洗，去重，存储等
        - pipeline需要处理process_item函数
            - process_item:
                - spider提取出来的item作为参数传入，同时传入的还有spider
                - 此方法必须实现
                - 必须返回一个Item对象，被丢弃的item不会被之后的pineline处理
            - __init__:构造函数
                - 进行一些必要的参数初始化
            - open_spider(spider):
                - spider对象被开启的时候调用
            - close_spider(spider):
                - 当spider对象被关闭的时候调用
- Spider
    - 对应的是文件夹spiders
    - __init__:初始化爬虫名称，start_urls列表
    - start_requests:生成Requests对象交给Scrapy下载并response
    - parse:根据返回的reponse解析出相应的item,item自动进入pipeline:如果需要，
    解析出url,url自动交给request模块，一直循环下去
    - start_request:此方法仅能被调用1次，读取start_urls内容并启动循环过程
    - name:设置爬虫名称
    - start_urls:设置开始第一批爬取的url
    - allow_domains:spider允许爬取的域名列表
    - start_request(self):只能被调用1次
    - parse
    - log:日志记录
- 中间件(DownloaderMiddlewares)      
    - 中间件是出于引擎和下载器中间的一层组件 
    - 可以有很多个，被按顺序加载执行
    - 作用是对发出的请求和返回的结果进行预处理
    - 在midelewares文件中
    - 需要在settings中设置以便生效
    - 一般一个中间件完成一项功能
    - 必须实现以下一个或者多个方法
        - process_request(self, request, spider)
            - 在request通过的时候被调用
            - 必须返回None或者Response或Request或raise IgnoreRequest
            - None:scrapy将继续处理该request
            - Request:scrapy会停止调用process_request并冲洗调度返回的request
            - Response:scrapy不会调用其他的process_request或者process_exception,直接让该response作为结果
            同时会调用process_response函数
        - process_response(self, request, respones,spider)
            - 跟process_request大同小异
            - 每次返回结果的时候会自动调用
            - 可以有多个，按照顺序调用
- 去重
    - 为了防止爬虫陷入死循环，需要去重
    - 即在spider中的parse函数中，返回Request的时候加上dont_filter=False参数
        myspider(scrapy.Spider):
            def parse(......)
                ......
                yield scrapy.Request(url=url,callback=self.parse, dont_filter=False)
                
- 如何在scrapy使用selenium
    - 可以放入中间件中的process_request函数中
    - 在函数中调用selenium,完成爬取后返回Response
        class MyMiddleWare(object)   
            def process_request(......)
                driver = webdriver.Chrome() 
                html = driver.page_source
                driver.quit()
                - 不再经过download，直接返回
                return HtmlResponse(url=request.url,encoding='utf-8',body=html,request=request)    
    
# scrapy-shell
- shell
- 启动
    - windows:active tl_django
    - scrapy shell "http://www.baidu.com"
    - 启动后自动下载指定的网页
    - 下载完成后，url内容保存在response的变量中，如果需要，我们需要调用response
- response
    - 爬取到的内容保存在response中给
    - response.body是网页的代码
    - reponse.headers是返回的http头信息
    - response.xpath允许使用xpath语法选择内容
    - reponse.css()允许使用css语法选择内容
- selector
    - 选择器、允许用户使用选择器来选择自己想要的内容
    - response.selector.xpath:response.xpath是selector.xpath的快捷方式
    - response.selector.css:response.css是他的快捷方式
    - selector.extract:把节点的内容用unicode的形式返回
    - selector.re:允许用户通过正则爬取选区内容

# 分布式爬虫
- 单机爬虫的问题
    - 单机效率
    - IO吞吐量
- 多爬虫问题
    - 数据共享
    - 在控件不同的多台电脑，可以成为分布式
- 需要做
    - 共享队列
    - 去重
- Redis
    - 内存数据库
    - 同时可以落地保存到硬盘
    - 可以去重
    - 可以把他理解成一共dict, set， list的集合体
    - 可以对保存的内容进行生命周期控制
    
- 内容保存数据库
    - MongoDB
    - Mysql等传统关系数据库
    
- 安装scrapy_redis
    - pip install 安装scrapy_redis
    - github.com/rolando/scrapy-redis
    - scrapy-redis.readthedocs.org
# 推荐书籍
- Python爬虫开发与项目实战，范传辉，机械工业出版社
- 精通python爬虫框架scrapy，李斌 翻译， 人民邮电出版社
- 崔庆才 

        