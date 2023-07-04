import json
from crawlers.crawler import Crawler
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from crawlers.unit import Unit


class CamdenRaineyCrawler(Crawler):
    BASE_URL = 'https://www.camdenliving.com'
    COMMUNITY = 'Camden Rainey Street'
    FEES = 96

    def __init__(self, driver: uc.Chrome):
        self.driver = driver

    def crawl(self):
        available_apartments_url = f'{self.BASE_URL}/apartments/austin-tx/camden-rainey-street/available-apartments'
        self.driver.get(available_apartments_url)
        floor_plan_urls = [e.get_attribute('href')
                           for e in self.driver.find_elements(By.CSS_SELECTOR, 'a.floor-plan-card-see-more-button')]
        for url in floor_plan_urls:
            self.driver.get(url)
            next_data = json.loads(self.driver.find_element(
                By.ID, '__NEXT_DATA__').get_attribute('innerHTML'))
            floor_plan_info = next_data['props']['pageProps']['data']['floorPlan']
            model = floor_plan_info['name']
            bedrooms = floor_plan_info['bedrooms'].replace('Studio', '0')
            bathrooms = floor_plan_info['bathrooms']
            floor_plan_id = floor_plan_info['realPageFloorPlanId']
            floor_plan_slug = floor_plan_info['slug']
            for unit_info in floor_plan_info['units']:
                unit = unit_info['unitName']
                area = unit_info['squareFeet']
                rent = unit_info['monthlyRent']
                url = f'{available_apartments_url}/{floor_plan_slug}-floor-plan?unit={unit}&floor={floor_plan_id}'
                yield Unit(url, self.COMMUNITY, model, bedrooms, bathrooms, unit, area, rent, self.FEES)
