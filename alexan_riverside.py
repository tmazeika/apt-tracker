import undetected_chromedriver as uc
from alexan_template import crawlTemplate


def crawl(driver: uc.Chrome):
    crawlTemplate(driver, 'https://alexanriverside.com', 'Alexan Riverside', 100)