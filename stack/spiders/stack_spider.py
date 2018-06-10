from scrapy import Spider, Selector

from stack.items import StackItem


class StackSpider(Spider):
	"""
	Defined Spider to retrieve last 50 questions from stack overflow.
	"""
	name = "stack"
	allowed_domains = ["stackoverflow.com"]
	start_urls = [
		"http://stackoverflow.com/questions?pagesize=50&sort=newest",
	]

	def parse(self, response):
		"""
		Extract title and link from scraped data.
		"""
		questions = Selector(response).xpath('//div[@class="summary"]/h3')
		for question in questions:
			item = StackItem()

			item['title'] = question.xpath(
				'a[@class="question-hyperlink"]/text()').extract()[0]
			item['url'] = question.xpath(
				'a[@class="question-hyperlink"]/@href').extract()[0]
			yield item
