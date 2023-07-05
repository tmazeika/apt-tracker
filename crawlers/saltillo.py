import re
from time import sleep
from crawlers.crawler import Crawler
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from util import extract_int
from crawlers.unit import Unit


class SaltilloCrawler(Crawler):
    BASE_URL = 'https://sonderyaustin.com'
    COMMUNITY = 'Residences at Saltillo'
    FEES = 70

    def __init__(self, driver: uc.Chrome):
        self.driver = driver

    def crawl(self):
        self.driver.get(f'https://residencesatsaltillo.prospectportal.com/austin/residences-at-saltillo')
        floorplan_urls = [e.get_attribute('content')
                          for e in self.driver.find_elements(By.CSS_SELECTOR, 'meta[itemprop="url"]')]
        for url in set(floorplan_urls):
            floorplan_id = re.search(r'floorplans/\w+-(\d+)', url).group(0)
            self.driver.get(f'https://residencesatsaltillo.prospectportal.com/?module=check_availability&is_secure=1&property[id]=706698&action=view_unit_spaces&property_floorplan[id]={floorplan_id}&move_in_date=true&term_month=15&occupancy_type=conventional')
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
