import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re
from util import printUnitInfo


def crawlFloorplan(driver: uc.Chrome, url: str, community: str, fees: int):
    driver.get(url)
    model = driver.find_element(By.XPATH, '//div[@class="floorplan-section"]/div[1]/div[1]/h2[1]').text
    bedroomsText = driver.find_element(By.XPATH, '//div[@class="floorplan-section"]/div[1]/div[1]/div[1]/span[1]').text
    bedrooms = int(re.search(r'(\d+)', bedroomsText.replace('Studio', '0')).group(1))
    bathroomsText = driver.find_element(By.XPATH, '//div[@class="floorplan-section"]/div[1]/div[1]/div[1]/span[2]').text
    bathrooms = int(re.search(r'(\d+)', bathroomsText).group(1))

    for e in driver.find_elements(By.XPATH, '//tr[@class="unit-container"]'):
        unit = re.search(r'(\d+)', e.find_element(By.XPATH, './td[@class="td-card-name"]').text).group(1)
        area = int(e.find_element(By.XPATH, './td[@class="td-card-sqft"]').text.replace(',', ''))
        rent = int(re.search(r'(\d+)', e.find_element(By.XPATH, './td[@class="td-card-rent"]').text.replace(',', '')).group(1))
        printUnitInfo(url, community, model, bedrooms, bathrooms, unit, area, rent, fees)


def crawlTemplate(driver: uc.Chrome, url: str, community: str, fees: int):
    driver.get(f'{url}/floorplans')
    urls = [e.get_attribute('href') for e in driver.find_elements(By.XPATH, '//a[contains(text(), "Availability")]')]
    for url in set(urls):
        crawlFloorplan(driver, url, community, fees)