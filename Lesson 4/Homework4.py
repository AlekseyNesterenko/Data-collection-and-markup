# Выберите веб-сайт с табличными данными, который вас интересует.
# Напишите код Python, использующий библиотеку requests для отправки HTTP GET-запроса на сайт 
# и получения HTML-содержимого страницы.
# Выполните парсинг содержимого HTML с помощью библиотеки lxml, чтобы извлечь данные из таблицы.
# Сохраните извлеченные данные в CSV-файл с помощью модуля csv.

# Ваш код должен включать следующее:

# Строку агента пользователя в заголовке HTTP-запроса, чтобы имитировать веб-браузер
#  и избежать блокировки сервером.
# Выражения XPath для выбора элементов данных таблицы и извлечения их содержимого.
# Обработка ошибок для случаев, когда данные не имеют ожидаемого формата.
# Комментарии для объяснения цели и логики кода.

# Примечание: Пожалуйста, не забывайте соблюдать этические и юридические нормы при веб-скреппинге.


import requests
from lxml import html
import csv
import unicodedata

resp = requests.get(url='https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2_%D0%B8_%D0%B7%D0%B0%D0%B2%D0%B8%D1%81%D0%B8%D0%BC%D1%8B%D1%85_%D1%82%D0%B5%D1%80%D1%80%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D0%B9_%D0%BF%D0%BE_%D0%BD%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8E', 
                    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'})

tree = html.fromstring(html=resp.content)

# выберем все данные по странм за исключением первой строки, которыая содержит заголовки.
countries = tree.xpath("//table[@class ='standard sortable']/tbody/tr")[1:]

# для проверки количества полученным стран. 
# print(len(countries)) 

# пустой список для стран
all_countries = []

# каждый атрибут обработаем через try-except для избежания ошибок, и запакуем их в словарь для кадой страны

for country in countries:
    try:
        name = country.xpath(".//span[contains(@class, 'nowrap')]/@data-sort-value")
        if name:
            name = name[0]
        else:
            name = country.xpath(".//td/a/@title")
            if name:
                name = name[0]
    except:
        name = ''
    
    try:
        population = country.xpath(".//td[position() = 3]/text()")
        if population:
            # библиотека unicodedata используется для удаления неразрывного пробела - "\xa0"
            population = unicodedata.normalize("NFKC", population[0])
    except:
        population = ''
    
    try:
        assessment_date = country.xpath(".//td[contains(@style, 'text-align:right')]/text()")[1]
    except:
        assessment_date = ''
    
    try:
        earth_population_percentage = country.xpath(".//td[position() = 5]/text()")
        if earth_population_percentage:
            earth_population_percentage = unicodedata.normalize("NFKC", earth_population_percentage[0])
    except:
        earth_population_percentage = ''
   
    m = {
        'name' : name,
        'population' : population,
        'assessment_date' : assessment_date,
        'Earth_population_percentage' : earth_population_percentage
    }

    all_countries.append(m)

# Сохраним в csv:
with open('all_countries.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['name', 'population', 'assessment_date', 'Earth_population_percentage']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    for row in all_countries:
        writer.writerow(row)

print(all_countries)

# Метод сохраения данных через библиотеку pandas:
# import pandas as pd

# df = pd.DataFrame(all_countries)
# df.to_csv('all_countries.csv', encoding='utf-8')