import scrapy

from scrapy.loader import ItemLoader
from ..items import PachicoItem


class PachicoSpider(scrapy.Spider):
	name = 'pachico'
	start_urls = ['https://pachico.net/blog']

	def parse(self, response):
		post_links = response.xpath('//article/a/@href')
		yield from response.follow_all(post_links, self.parse_post)

		pagination_links = response.xpath('//div[@class="nav-previous"]/a/@href')
		yield from response.follow_all(pagination_links, self.parse)

	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//div[@class="entry-content container"]/div/div/h2/text()|//div[@class="entry-content container"]/div/div/p/text()').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description)

		item = ItemLoader(item=PachicoItem(), response=response)
		item.add_value('title', title)
		item.add_value('description', description)

		return item.load_item()