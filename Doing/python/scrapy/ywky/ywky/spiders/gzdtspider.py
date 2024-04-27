import scrapy

class GzdtspiderSpider(scrapy.Spider):
    name = 'gzdtspider'
    allowed_domains = ['ywky.edu.cn']
    start_urls = ['http://www.ywky.edu.cn/list.html?kid=15']

    def parse(self, response):
        # 提取每个新闻的标题和链接
        for news in response.css('.list-box ul li'):
            title = news.css('a::text').get()
            link = news.css('a::attr(href)').get()

            # 检查是否成功提取了标题和链接
            if title and link:
                # 构造绝对 URL
                absolute_url = response.urljoin(link)

                # 产生一个 Request 对象，跟踪链接，并使用 parse_article 方法处理响应
                yield scrapy.Request(url=absolute_url, callback=self.parse_article, meta={'title': title})
            else:
                # 如果提取标题或链接失败，输出一条日志
                self.logger.warning(f'Failed to extract title or link from {news.get()}')

        # 处理分页，提取 "下一页" 的链接
        next_page = response.css('.list-box .pagebar a:last-child::attr(href)').get()
        if next_page:
            # 如果找到了 "下一页" 链接，构造绝对 URL，并产生一个 Request 对象
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
