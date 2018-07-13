# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class QuizSpider(CrawlSpider):
    name = 'quiz'
    allowed_domains = ['hqbuff.com']
    start_urls = ['https://hqbuff.com/game/2018-07-13']

    rules = (
        Rule(LinkExtractor(), callback='parse', follow=True),
    )
    def parse(self, response):
        blocks = response.xpath('//*[@class="question"]')
        for block in blocks:
            questions = block.xpath('.//*[@class="question__text"]/text()').extract_first()
            options = block.xpath('.//ul[@class="questions"]/li/text()').extract()
            answers = block.xpath('.//*[@class="questions__correct"]/text()').extract_first()

            yield{'Question': questions,
                  'Options': options,
                  'Answer': answers }

        #Get next page url 
        next_page_url = response.xpath('//*[@class="nav-item"]/a/@href').extract_first()
        abs_next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(abs_next_page_url)
