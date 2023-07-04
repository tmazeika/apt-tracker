import re
from crawlers.crawler import Crawler
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from util import extract_int
from crawlers.unit import Unit


class SkyHouseCrawler(Crawler):
    BASE_URL = 'https://skyhouseaustin.securecafe.com/onlineleasing/skyhouse-austin/oleapplication.aspx'
    COMMUNITY = 'SkyHouse'
    FEES = 70

    def __init__(self, driver: uc.Chrome):
        self.driver = driver

    def crawl(self):
        self.driver.get(
            f'{self.BASE_URL}?stepname=floorplan&myOlePropertyId=160565')
        floorplan_js_urls = [e.get_attribute('onclick').split("'")[1]
                             for e in self.driver.find_elements(By.CSS_SELECTOR, '#floorplanlist .applyButton')]
        for url in set(floorplan_js_urls):
            yield from self.__crawl_floorplan(url)

    def __crawl_floorplan(self, url: str):
        self.driver.get(url)
        description_text = self.driver.find_element(
            By.CSS_SELECTOR, '.row-fluid > .block > .row-fluid > div > h3').text
        description_match = re.search(
            r'FLOOR PLAN : (\w+) - (\d+) BEDROOMS?, (\d+) BATHROOMS?', description_text)
        model = description_match.group(1)
        bedrooms = int(description_match.group(2))
        bathrooms = int(description_match.group(3))

        for e in self.driver.find_elements(By.CSS_SELECTOR, 'tr.AvailUnitRow'):
            unit = e.find_element(By.XPATH, './td[1]').text[1:]
            area = e.find_element(By.XPATH, './td[2]').text
            rent = extract_int(e.find_element(By.XPATH, './td[3]').text)
            yield Unit(url, self.COMMUNITY, model, bedrooms, bathrooms, unit, area, rent, self.FEES)
