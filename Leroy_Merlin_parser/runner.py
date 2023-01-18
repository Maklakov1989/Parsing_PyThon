from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging

from Leroy_Merlin_parser.spiders.Leroy_Merlin import LeroyMerlinSpider

if __name__ == '__main__':
    configure_logging()
    settings = get_project_settings()
    runner = CrawlerRunner(settings)
    search = input('Что вы хотите найти: ')
    runner.crawl(LeroyMerlinSpider, search=search)

    d = runner.join()
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
