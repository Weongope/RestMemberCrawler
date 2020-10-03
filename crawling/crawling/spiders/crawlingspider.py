import scrapy
from urllib.parse import urljoin
from crawling.items import CrawlingItem
import jsonschema
import json

class CrawlingSpider(scrapy.Spider):
    
    name = "crawling"
    
    start_urls = [
        "https://www.parliament.bg/bg/MP"
    ]

    def parse(self, response):      
     
        for mp in response.css('.MPinfo a::attr(href)').extract():
            url = urljoin("https://www.parliament.bg/", mp)
            yield scrapy.Request(url, callback = self.parse_minister)
    
    def parse_minister(self, response):
        person = CrawlingItem()
        separator = " " 

        main_information = response.css(".MPinfo li")       
        
        name = separator.join(response.css(".MProwD strong::text").getall()).title()
        birth_date = ""
        birth_place = ""
        profession = ""
        languages = ""
        political_force = ""
        email = ""
        
        for info in main_information:
            if "Дата на раждане" in str(info) : 
                birth_date = info.css("::text").get().split()[4]
                birth_place = separator.join(info.css("::text").get().split()[5:])
            if "Професия" in str(info):
                profession = ", ".join(info.css("::text").get().split()[1].split(";")[:-1]).title()
                
            if "Езици" in str(info):
                languages = ", ".join(info.css("::text").get().split()[1].split(";")[:-1]).title()
                
            if "политическа сила" in str(info):
                political_force = separator.join(info.css("::text").get().split()[4:-1])
                
            if "E-mail" in str(info):
                email = info.css("::text")[1].get()
        
        person["name"] = name
        person["birth_date"] = birth_date
        person["birth_place"] = birth_place
        person["profession"] = profession
        person["languages"] = languages
        person["political_force"] = political_force
        person["email"] = email
        
        with open('crawling\schemas.json') as json_file:
            data = json.load(json_file)
        
        jsonschema.validate(dict(person), data)
        return person       