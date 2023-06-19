import undetected_chromedriver as uc
from windsor_template import crawlTemplate


def crawl(driver: uc.Chrome):
    crawlTemplate(driver, 'https://www.windsorsoco.com', 'Windsor South Congress', 0)