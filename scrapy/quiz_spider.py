# -*- coding: utf-8 -*-
import scrapy

class SpideySpider(scrapy.Spider):
    name = 'spidey'
    allowed_domains = ['https://hqbuff.com/game/2018-07-10/3']
    start_urls = ['https://hqbuff.com/game/2018-07-10/3']

    def parse(self, response):
        blocks = response.xpath('//*[@class="question"]')
        for block in blocks:
            questions = block.xpath('.//*[@class="question__text"]/text()').extract_first()
            options = block.xpath('.//ul[@class="questions"]/li/text()').extract()
            answers = block.xpath('.//*[@class="questions__correct"]/text()').extract_first()

            '''
            print ('\n')
            print(questions)
            print(options)
            print(answers)
            print('\n')
            '''

            yield{'Question': questions,
                  'Options': options,
                  'Answer': answers }
       