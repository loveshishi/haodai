# -*- coding: utf-8 -*-
import re
from time import sleep

import scrapy
from bs4 import BeautifulSoup
from scrapy import Request

from haodai.items import HaodaiItem



class HhspiderSpider(scrapy.Spider):
    name = 'hhspider'
    allowed_domains = ['www.haodai.com']
    start_urls = ['http://www.haodai.com/loan/']
    money = [5,10,15,20,25,30]
    month = [3,6,12,18,24,36]

    def parse(self, response):
        alist = response.xpath("//div[@id='city_box']//dd/a")
        for a in alist:
            href = a.xpath("./@href").extract()[0]
            for money in self.money:
                for month in self.month:
                    nexthref = href+"/s4-"+str(money)+"x"+str(month)+"-0x0x9999/"
                    request = Request(nexthref,callback=self.parse_href,dont_filter = True)
                    request.meta['href'] = href
                    yield request

    def parse_href(self,response):
        lists = response.xpath('//div[@class="ma_nr"]')
        for list in lists:
            url = list.xpath(".//span/a/@href").extract_first()
            gongsi_id = re.findall("/(\d+x\d+x\d+?)\.", url)[0]
            gongsi_img = response.meta['href'] + list.xpath(".//span/a/img/@src").extract_first()
            the_method = list.xpath(".//p[@class='jqtap co9']/a/@title").extract_first()
            appraise = list.xpath(".//samp/p[@class='Pstars']/span/em/@class").extract_first()
            require = list.xpath(".//div[@class='con04']/p/text()").extract()
            requirements = ";".join(require)
            chara = list.xpath(".//ul[@class='icon']/li/a/@title").extract()
            charas = ";".join(chara)
            # 产品特点图片
            chara_img = list.xpath(".//ul[@class='icon']/li/a/@style").extract()
            chara_imgs = ";".join(chara_img)
            alls = re.findall("\'(.*?)\'", chara_imgs)
            charas_img = ""
            for imgurl in alls:
                charas_img += response.meta['href'] + imgurl + ";"
            request = Request(url, callback=self.parse_data,dont_filter=True)
            request.meta['cid'] = gongsi_id
            request.meta['gongsi_img'] = gongsi_img
            request.meta['the_method'] = the_method
            request.meta['evaluation'] = appraise
            request.meta['requirements'] = requirements
            request.meta['charas'] = charas
            request.meta['charas_img'] = charas_img
            yield request

    def parse_data(self,response):
        daikuan = HaodaiItem()
        daikuan['cid'] = response.meta['cid']
        daikuan['url'] = response.url
        daikuan['name'] = response.xpath("//span[@class='cpsp1']/text()").extract_first()
        content_one = response.xpath("//td[@class='cptd2']/text()").extract()
        money = re.findall('\d+', content_one[0])[0]
        daikuan['money'] = int(money)
        term_time = re.findall('\d+', content_one[1])[0]
        daikuan['timeran'] = int(term_time)
        month_supply = re.findall('\d+', content_one[2])[0]
        daikuan['month_pay'] = int(month_supply)
        total_post = re.findall('(.*?)万元', content_one[3])[0]
        daikuan['sum_money'] = float(total_post)
        ls = response.xpath("//td[@class='cptd2']//span/text()").extract()
        daikuan['description'] = " ".join(ls[1:])
        content2 = response.xpath("//td[@class='cptd4']/text()").extract()
        daikuan['mon_range'] = content2[0]
        daikuan['termtime_range'] = content2[1]
        daikuan['pay_style'] = content2[2]
        loan_time = re.findall('(\d+)', content2[3])[0]
        daikuan['loan_time'] = int(loan_time)
        number = response.xpath("//div[@class='success_sqrs']/span/text()").extract_first()
        daikuan['man_num'] = str(number)
        content3 = response.xpath("//div[@class='kuai']/p[2]")
        li1 = content3[0].xpath('./text()').extract()
        daikuan['man_condition'] = " ".join(li1)
        li2 = content3[1].xpath('./text()').extract()
        daikuan['material'] = " ".join(li2)
        li3 = content3[2].xpath('./text()').extract()
        daikuan['all_explain'] = " ".join(li3)
        daikuan['gongsi_img'] = response.meta['gongsi_img']
        daikuan['loan_style'] = response.meta['the_method']
        daikuan['evaluation'] = response.meta['evaluation']
        daikuan['requirements'] = response.meta['requirements']
        daikuan['charas'] = response.meta['charas']
        daikuan['charas_img'] = response.meta['charas_img']
        yield daikuan