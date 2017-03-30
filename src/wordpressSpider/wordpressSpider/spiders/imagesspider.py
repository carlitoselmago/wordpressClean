# import the necessary packages
from wordpressSpider.items import WordpressspiderItem
import datetime
import scrapy
from scrapy.http    import Request 
#import urllib, os


class ImagesSpider(scrapy.Spider):
	name = "wordpressImages"
	start_urls = ["http://www.alpino.eu/alpino/"]
        
        imgsData = open('images.csv','a')
        linkData = open('links.csv','a')
        pdfsData = open('pdfs.csv','a')
        
        def parse(self, response):
            
                crawledLinks = []
                crawledImages= []
                crawledPdfs= []
            
		# let's only gather Time U.S. magazine covers
		images = response.css('img').xpath('@src').extract()
                
                if images:
                    for url in images:
                        if url not in crawledImages:
                            print url+":::::::::::::::"
                            self.imgsData.write(url+"\n")
                            """
                            THE ACTION

                            """
                            crawledImages.append(url)
                        
                        
                        
                    
                links= response.css('a').xpath('@href').extract()
                
                if links:
                    for link in links:
                        if ".pdf" in link:
                            if link not in crawledPdfs:
                                crawledPdfs.append(link)
                                self.pdfsData.write(link+"\n")
                        else:
                            if link not in crawledLinks:
                                if "http://www.alpino.eu" in link:
                                    crawledLinks.append(link)
                                    self.linkData.write(link+"\n")
                                    yield Request(link, self.parse)
                        
                
		#yield scrapy.Request(url.extract_first(), self.parse_page)
                
        """
        def parse_page(self, response):
		# loop over all cover link elements that link off to the large
		# cover of the magazine and yield a request to grab the cove
		# data and image
		for href in response.xpath('@src'):
			yield scrapy.Request(href.extract_first(),
				self.parse_covers)
 
		# extract the 'Next' link from the pagination, load it, and
		# parse it
		next = response.css("div.pages").xpath("a[contains(., 'Next')]")
		yield scrapy.Request(next.xpath("@href").extract_first(), self.parse_page)"""
                