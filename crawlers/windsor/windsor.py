from crawlers.crawler import Crawler
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from util import extract_int
from crawlers.unit import Unit


class WindsorCrawler(Crawler):
    def __init__(self, driver: uc.Chrome, base_url: str, community: str, fees: int):
        self.driver = driver
        self.base_url = base_url
        self.community = community
        self.fees = fees

    def crawl(self):
        self.driver.get(f'{self.base_url}/floorplans')
        floorplan_urls = [e.get_attribute('href')
                          for e in self.driver.find_elements(By.XPATH, '//a[contains(text(), "Availability")]')]
        for url in set(floorplan_urls):
            yield from self.__crawl_floorplan(url)

    def __crawl_floorplan(self, url: str):
        self.driver.get(url)
        model = self.driver.find_element(
            By.XPATH, '//div[@class="floorplan-section"]/div[1]/div[1]/h2[1]').text
        bedrooms_text = self.driver.find_element(
            By.XPATH, '//div[@class="floorplan-section"]/div[1]/div[1]/div[1]/span[1]').text
        print(bedrooms_text)
        print(url)
        bedrooms = extract_int(bedrooms_text.replace('Studio', '0'))
        bathrooms_text = self.driver.find_element(
            By.XPATH, '//div[@class="floorplan-section"]/div[1]/div[1]/div[1]/span[2]').text
        bathrooms = extract_int(bathrooms_text)

        for e in self.driver.find_elements(By.XPATH, '//tr[@class="unit-container"]'):
            unit = extract_int(e.find_element(
                By.XPATH, './td[@class="td-card-name"]').text)
            area = extract_int(e.find_element(
                By.XPATH, './td[@class="td-card-sqft"]').text)
            rent = extract_int(e.find_element(
                By.XPATH, './td[@class="td-card-rent"]').text)
            yield Unit(url, self.community, model, bedrooms, bathrooms, unit, area, rent, self.fees)
