import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re
from util import printCsvLine


def crawlFloorplan(driver: uc.Chrome, url: str, community: str, fees: int):
    driver.get(url)
    model = driver.find_element(By.XPATH, '//section[@class="content plan"]/div[1]/div[1]/div[2]/h2[1]').text
    descriptionText = driver.find_element(By.XPATH, '//section[@class="content plan"]/div[1]/div[1]/div[2]/h4[1]').text
    descriptionMatch = re.search(r'(\d+) BED \| ([\d\.]+) BATH \| (\d+) SF', descriptionText.replace('STUDIO', '0 BED'))
    bedrooms = descriptionMatch.group(1)
    bathrooms = descriptionMatch.group(2)
    area = int(descriptionMatch.group(3))

    for e in driver.find_elements(By.XPATH, '//tr[@class="avail-units"]'):
        unit = e.find_element(By.XPATH, './td[1]').text
        rent = int(re.search(r'(\d+)', e.find_element(By.XPATH, './td[2]').text.replace(',', '')).group(1))
        totalRent = rent + fees
        rentPerArea = f'{totalRent / area:.2f}'
        printCsvLine(url, community, model, bedrooms, bathrooms, unit, area, rent, fees, totalRent, rentPerArea)


def crawlTemplate(driver: uc.Chrome, url: str, community: str, fees: int):
    driver.get(f'{url}/floor-plans')
    urls = [e.get_attribute('href').replace('?move=', '') \
            for e in driver.find_elements(By.XPATH, '//a[contains(text(), "View Details")]')]
    for url in set(urls):
        crawlFloorplan(driver, url, community, fees)