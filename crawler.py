import re
import json
import argparse
from urllib.parse import urlparse

import logging
from scrapy import Spider
from scrapy.crawler import CrawlerProcess
from twisted.internet.error import DNSLookupError


logging.getLogger('scrapy').propagate = False


class ParaSpider(Spider):
    name = "paragraph_spider"

    history = []
    log = dict(pages=[])
    log_file = 'log.json'
    

    def parse(self, response):
        self.history.append(response.url)
        content = ''
        
        try:
            for p in response.xpath('//p//text()').extract():
                content += f'{p} '
            

            page = {
                'page': response.url,
                'content': content
            }

            self.log['pages'].append(page)

            
            for next_page in response.css('a::attr(href)').extract():
                if next_page not in self.history:
                    yield response.follow(next_page, callback=self.parse)
            

            print(f'parsed {response.url} ..')
        except:
            print(f'skipping {response.url} ..')
    

    def closed(self, reason):
        with open(self.log_file, 'w+', encoding="utf-8") as f:
            json.dump(self.log, f, ensure_ascii=False)
            print(f'\ngenerated {self.log_file}')



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("url", nargs=1, help="url to start crawling from", type=str)
    parser.add_argument("-o", nargs=1, help="specify output file; will be generated if does not exist, will truncate previous data if exists", default="log.json", type=str, metavar='--output')

    args = parser.parse_args()
    
    url = str(args.url)
    url = url.strip('\"')
    url = url.strip('\'')

    if not url.startswith('http'):
        url = f'http://{url}'

    parsable_url = urlparse(url)
    
    start_urls = [url]
    allowed_domains = (parsable_url.netloc,)

    log_file = args.o

    runner = CrawlerProcess()
    runner.crawl(ParaSpider, allowed_domains=allowed_domains, start_urls=start_urls, log_file=log_file)
    runner.start()