from crawlers.windsor.windsor import WindsorCrawler
import undetected_chromedriver as uc


class WindsorElevenCrawler(WindsorCrawler):
    def __init__(self, driver: uc.Chrome):
        super().__init__(driver, 'https://www.elevenbywindsor.com', 'Eleven', 70)
