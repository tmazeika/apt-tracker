import undetected_chromedriver as uc
from windsor_template import crawlTemplate


def crawl(driver: uc.Chrome):
    crawlTemplate(driver, 'https://www.elevenbywindsor.com', 'Eleven', 45+25)