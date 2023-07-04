from crawlers.windsor.windsor import WindsorCrawler
import undetected_chromedriver as uc


class WindsorSocoCrawler(WindsorCrawler):
    def __init__(self, driver: uc.Chrome):
        super().__init__(driver, 'https://www.windsorsoco.com', 'Windsor South Congress', 0)
