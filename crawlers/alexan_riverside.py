from crawlers.crawler import Crawler
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import re
from util import extract_int
from crawlers.unit import Unit


class AlexanRiversideCrawler(Crawler):
    BASE_URL = 'https://alexanriverside.com'
    COMMUNITY = 'Alexan Riverside'
    FEES = 100

    def __init__(self, driver: uc.Chrome):
        self.driver = driver

    def crawl(self):
        self.driver.get(f'{self.BASE_URL}/floor-plans')
        floorplan_urls = [e.get_attribute('href').replace('?move=', '')
                          for e in self.driver.find_elements(By.XPATH, '//a[contains(text(), "View Details")]')]
        for url in set(floorplan_urls):
            yield from self.__crawl_floorplan(url)

    def __crawl_floorplan(self, url: str):
        self.driver.get(url)
        model = self.driver.find_element(
            By.XPATH, '//section[@class="content plan"]/div[1]/div[1]/div[2]/h2[1]').text
        description_text = self.driver.find_element(
            By.XPATH, '//section[@class="content plan"]/div[1]/div[1]/div[2]/h4[1]').text
        description_match = re.search(
            r'(\d+) BED \| ([\d\.]+) BATH \| (\d+) SF', description_text.replace('STUDIO', '0 BED'))
        bedrooms = int(description_match.group(1))
        bathrooms = int(description_match.group(2))
        area = int(description_match.group(3))

        for e in self.driver.find_elements(By.XPATH, '//tr[@class="avail-units"]'):
            unit = e.find_element(By.XPATH, './td[1]').text
            rent = extract_int(e.find_element(By.XPATH, './td[2]').text)
            yield Unit(url, self.COMMUNITY, model, bedrooms, bathrooms, unit, area, rent, self.FEES)
