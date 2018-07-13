# -*- coding: utf-8 -*-
import scrapy


class QuizSpider(scrapy.Spider):
    name = 'quiz'
    allowed_domains = ['hqbuff.com']
    start_urls = ['http://hqbuff.com/game/2018-05-08/1']

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
        
        '''next_page_url = response.xpath('/html/body/div[1]/ul/li[3]/a/@href').extract()
        abs_next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(abs_next_page_url)'''
