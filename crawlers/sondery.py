from time import sleep
from crawlers.crawler import Crawler
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from util import extract_int
from crawlers.unit import Unit


class SonderyCrawler(Crawler):
    BASE_URL = 'https://sonderyaustin.com'
    COMMUNITY = 'Sondery'
    FEES = 70

    def __init__(self, driver: uc.Chrome):
        self.driver = driver

    def crawl(self):
        self.driver.get(f'{self.BASE_URL}/floorplans')
        floorplan_urls = [e.get_attribute('href')
                          for e in self.driver.find_elements(By.XPATH, '//div[@class="skylease"]/ul/li/a')]
        for url in set(floorplan_urls):
            yield from self.__crawl_floorplan(url)

    def __crawl_floorplan(self, url: str):
        self.driver.get(url)
        btns = self.driver.find_elements(
            By.CSS_SELECTOR, 'a.skylease-unit__button')
        if len(btns) < 2:
            return
        btns[1].click()
        sleep(1)  # Waits for animation to finish.
        model = self.driver.find_element(
            By.CSS_SELECTOR, 'h1.skylease-unit__title').text
        description_text = self.driver.find_elements(
            By.CSS_SELECTOR, 'p.skylease-unit__info-content')
        bedrooms = int(description_text[0].text.replace(
            'Studio', '0').split(' ')[0])
        bathrooms = int(description_text[1].text.split(' ')[0])
        area = int(description_text[-1].text.split(' ')[0])

        for e in self.driver.find_elements(By.XPATH, '//table[@class="skylease-unit-table__table"]//tr')[1:]:
            if not e.find_elements(By.XPATH, './td[2]'):
                continue
            unit = e.find_element(By.XPATH, './td[2]').text[2:]
            rent = extract_int(e.find_element(By.XPATH, './td[4]').text)
            yield Unit(url, self.COMMUNITY, model, bedrooms, bathrooms, unit, area, rent, self.FEES)
