from crawlers.crawler import Crawler
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import re
from util import extract_int
from crawlers.unit import Unit


class AlexanWaterlooCrawler(Crawler):
    BASE_URL = 'https://www.alexanwaterloo.com/'
    COMMUNITY = 'Alexan Waterloo'
    FEES = 175

    def __init__(self, driver: uc.Chrome):
        self.driver = driver

    def crawl(self):
        self.driver.get(f'{self.BASE_URL}/austin/alexan-waterloo/conventional/')
        floorplan_urls = [e.get_attribute('href')
                          for e in self.driver.find_elements(By.XPATH, '//a[contains(text(), "View Details")]')]
        for url in set(floorplan_urls):
            yield from self.__crawl_floorplan(url)

    def __crawl_floorplan(self, url: str):
        self.driver.get(url)
        model = self.driver.find_element(
            By.CSS_SELECTOR, '.flex-between > h1:nth-child(1)').text
        description_text = self.driver.find_element(
            By.CSS_SELECTOR, '.details > ul:nth-child(1) > li:nth-child(1) > strong:nth-child(1)').text
        description_match = re.search(
            r'(\d+) Bed / ([\d\.]+) Bath', description_text.replace('Studio', '0'))
        bedrooms = int(description_match.group(1))
        bathrooms = int(float(description_match.group(2)))
        area_text = self.driver.find_element(
            By.CSS_SELECTOR, '.details > ul:nth-child(1) > li:nth-child(3)').text
        area = extract_int(area_text)

        for e in self.driver.find_elements(By.CSS_SELECTOR, '#available-units .option-row:not(.title)'):
            unit = e.find_element(By.CSS_SELECTOR, '.detail.first').text
            rent = extract_int(e.find_element(By.CSS_SELECTOR, '.detail.second:nth-child(4)').text)
            yield Unit(url, self.COMMUNITY, model, bedrooms, bathrooms, unit, area, rent, self.FEES)
