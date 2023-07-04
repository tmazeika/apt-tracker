from datetime import date
import re
import requests
from crawlers.crawler import Crawler
import undetected_chromedriver as uc
from crawlers.unit import Unit


class CorazonCrawler(Crawler):
    BASE_URL = 'https://www.corazonatxapartments.com'
    FLOOR_PLANS_URL = 'https://www.corazonatxapartments.com/Floor-plans.aspx'
    COMMUNITY = 'Corazon'
    FEES = 0

    def __init__(self, driver: uc.Chrome):
        self.driver = driver

    def crawl(self):
        available_units = requests.get(
            f'https://api.ws.realpage.com/v2/property/8966698/units?available=true&honordisplayorder=true&siteid=8966698&bestprice=true&leaseterm=3,4,5,6,7,8,9,10,11,12,13,14,15&dateneeded={date.today()}',
                headers = {'x-ws-authkey': '9b1b8ecd-386f-4c0e-ac63-5effdfce0877'}).json()['response']['units']
        for unit_info in available_units:
            model = re.search(r'(\w+)', unit_info['floorPlanImages'][0]['alt']).group(1).lower()
            bedrooms = int(unit_info['numberOfBeds'])
            bathrooms = int(unit_info['numberOfBaths'])
            unit = unit_info['name']
            area = int(unit_info['squareFeet'])
            rent = int(unit_info['rent'])
            yield Unit(self.FLOOR_PLANS_URL, self.COMMUNITY, model, bedrooms, bathrooms, unit, area, rent, self.FEES)
