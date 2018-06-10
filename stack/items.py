# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class StackItem(Item):
	"""
	Item to store title and question url from scraped data.
	"""
	title = Field()
	url = Field()