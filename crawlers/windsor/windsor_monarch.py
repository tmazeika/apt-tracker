from crawlers.windsor.windsor import WindsorCrawler
import undetected_chromedriver as uc


class WindsorMonarchCrawler(WindsorCrawler):
    def __init__(self, driver: uc.Chrome):
        super().__init__(driver, 'https://www.themonarchbywindsor.com', 'The Monarch', 185)
