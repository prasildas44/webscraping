# -*- coding: utf-8 -*-
import scrapy


class Reviews1Spider(scrapy.Spider):
    name = 'reviews1'
    allowed_domains = ['www.amazon.co.uk']
    start_urls = ['https://www.amazon.co.uk/All-new-Amazon-generation-Charcoal-Fabric/product-reviews/B06Y5ZW72J/ref=cm_cr_getr_d_paging_btm_1?ie=UTF8&reviewerType=all_reviews&pageNumber={}' .format(i) for i in range(1,5)]


    def parse(self, response):
        yield{
        	'author':response.xpath('//span[contains (@class,"a-profile-name")]/text()').extract(),
        	'title': response.xpath("//a[contains(@class,'a-size-base a-link-normal review-title a-color-base a-text-bold')]/text()").extract(),
        	'review': response.xpath("//div[contains (@class, 'a-expander-content a-expander-partial-collapse-content')]/text()").extract(),
        	'rating': response.xpath('//i[contains(@data-hook,"review-star-rating")]/span[contains(@class,"a-icon-alt")]/text()').extract(),
        	'useful':response.xpath('//span[contains(@data-hook,"helpful-vote-statement")]/text()').extract(),




        }
