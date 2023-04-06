#algo de scrap

import scrapy

class AlloCineSpider(scrapy.Spider):
    name = 'sens critique'
    allowed_domains = ['senscritique.com']
    start_urls = ['https://www.senscritique.com/films/tops/top100-des-top10']

    def parse(self, response):
        for film in response.css('div.ProductListItem__Container-sc-ico7lo-0.hZLWXB'):
            yield {
                'titre': film.css('h2.Text__SCText-sc-kgt5u3-0.gwWwBt a::text').get(),
                'producteur': film.css('a.Text__SCText-sc-kgt5u3-0.Link__PrimaryLink-sc-1vfcbn2-0.cBBiTW.dPapvk span::text').get(),
            }