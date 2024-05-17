import scrapy


class CountriesSpider(scrapy.Spider):
    name = "countries"
    allowed_domains = ["ru.wikipedia.org"]
    start_urls = ["https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2_%D0%B8_%D0%B7%D0%B0%D0%B2%D0%B8%D1%81%D0%B8%D0%BC%D1%8B%D1%85_%D1%82%D0%B5%D1%80%D1%80%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D0%B9_%D0%BF%D0%BE_%D0%BD%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8E"]

    def parse(self, response):
        countries = response.xpath("//table[contains(@class, 'standard sortable')]/tbody/tr")[1:]
        for country in countries:
            try:
                name = country.xpath(".//td/span[contains(@class, 'nowrap')]/@data-sort-value").get()
                if not name:
                    name = country.xpath(".//td/a/@title").get()
            except:
                name = ''
            
            try:
                population = country.xpath(".//td[position() = 3]/text()").get()
            except:
                population = ''
            
            try:
                assessment_date = country.xpath(".//td[contains(@style, 'text-align:right')]/text()")[1].get()
            except:
                assessment_date = ''
            
            try:
                earth_population_percentage = country.xpath(".//td[position() = 5]/text()").get()
            except:
                earth_population_percentage = ''
        
            yield {
                'name' : name,
                'population' : population,
                'assessment_date' : assessment_date,
                'Earth_population_percentage' : earth_population_percentage
            }

# scrapy crawl countries -o population.json
