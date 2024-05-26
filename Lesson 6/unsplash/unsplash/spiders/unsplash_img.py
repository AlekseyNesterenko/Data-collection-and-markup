import scrapy
from scrapy.loader import ItemLoader
from unsplash.items import ImgparserItem
from urllib.parse import urljoin


class UnsplashImgSpider(scrapy.Spider):
    name = "unsplash_img"
    allowed_domains = ["unsplash.com"]
    start_urls = ["https://unsplash.com"]

    # rules = (Rule(LinkExtractor(restrict_xpaths="//div[@class='zmDAx']"), 
    #               callback="parse_item", follow=True),)

    def parse(self, response):
        relative_url_categories = response.xpath("(//ul)[last()]//a[not(text()='Unsplash+') and not(text()='Editorial')]/@href").getall()
        url_categories = [urljoin("https://unsplash.com", img_url) for img_url in relative_url_categories]
        # print(url_categories)
        for category in url_categories:
            yield response.follow(url=category, callback=self.img_parse)

    def img_parse(self, response):
        list_url = response.xpath("//img[@data-test]")
        for item in list_url:
            # Создаем элемент loader
            loader = ItemLoader(item=ImgparserItem(), response=response)
            # Записываем в loader имя категории
            loader.add_xpath('category', '//h1/text()')
            # Записываем в переменные название и ссылку на картинку
            url = item.xpath('./@src').get()
            name = item.xpath('./@alt').get()
            # Записываем в loader ссылку на картинку и название
            loader.add_value('url', url)
            loader.add_value('name', name)
            # Посылаем loader в Pipeline
            yield loader.load_item()
