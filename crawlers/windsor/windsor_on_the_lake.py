from crawlers.windsor.windsor import WindsorCrawler
import undetected_chromedriver as uc


class WindsorOnTheLakeCrawler(WindsorCrawler):
    def __init__(self, driver: uc.Chrome):
        super().__init__(driver, 'https://www.windsoronthelake.com', 'Windsor on the Lake', 90)
