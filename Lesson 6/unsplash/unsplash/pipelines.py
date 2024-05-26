import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import hashlib
import os
from unsplash.settings import IMAGES_STORE, BOT_NAME


class PhotosPipeline(ImagesPipeline):
    count_img = 0
    def get_media_requests(self, item, info):
        
        try:
            # Выводим информацию о состоянии процесса
            self.count_img += 1
            print(f'Обработано {self.count_img} ссылок')
            yield scrapy.Request(item['url'])
        except Exception as e:
            print(e)
    def file_path(self, request, response=None, info=None, *, item=None):
        image_guid = hashlib.sha1(request.url.encode()).hexdigest()
        file_name = f"{item['name']}-{image_guid}.jpg"
        # Записываем полный путь к файлу
        basedir = str(os.path.abspath(os.path.dirname(__file__))).replace(BOT_NAME, '')
        file_path = os.path.join(basedir + IMAGES_STORE, file_name)
        item['path'] = f'{file_path}'
        return file_name
