# -*- coding: utf-8 -*-
import scrapy


class NoticiasDestaqueSpider(scrapy.Spider):
    name = 'noticias_destaque'
    allowed_domains = ['belem.ifpa.edu.br']
    start_urls = ['belem.ifpa.edu.br']

    def parse(self, response):
        for item in response.css("section"):
            # captura os links das imagens em destaque

            link = response.css("section#content-section a.img-rounded::attr(href)").extract()
            yield response.follow(link,self.parse_destaque)
        
    def parse_destaque(self,response):
        pass