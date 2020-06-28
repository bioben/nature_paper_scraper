import scrapy

class MainSpider(scrapy.Spider):
	name = "main_spider"
	start_urls = ['https://www.nature.com/search?q=alzheimer%27s+disease+microglia']

	def parse(self, response):
		selector = '.h3 extra-tight-line-height'
		for article in response.css(selector):

			NAME_SELECTOR = 'h2 ::text'
			yield {
				'name':article.css(NAME_SELECTOR).extract_first(),
			}