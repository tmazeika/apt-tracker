from crawlers.windsor.windsor import WindsorCrawler
import undetected_chromedriver as uc


class WindsorSouthLamarCrawler(WindsorCrawler):
    def __init__(self, driver: uc.Chrome):
        super().__init__(driver, 'https://www.windsorsola.com', 'Windsor South Lamar', 65)
