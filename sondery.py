from time import sleep
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re
from util import printCsvLine


def crawlFloorplan(driver: uc.Chrome, url: str, community: str, fees: int):
    driver.get(url)
    btns = driver.find_elements(By.CSS_SELECTOR, 'a.skylease-unit__button')
    if len(btns) < 2: return
    btns[1].click()
    sleep(1)
    model = driver.find_element(By.CSS_SELECTOR, 'h1.skylease-unit__title').text
    descriptionText = driver.find_elements(By.CSS_SELECTOR, 'p.skylease-unit__info-content')
    bedrooms = descriptionText[0].text.replace('Studio', '0').split(' ')[0]
    bathrooms = descriptionText[1].text.split(' ')[0]
    area = int(descriptionText[-1].text.split(' ')[0])

    for e in driver.find_elements(By.XPATH, '//table[@class="skylease-unit-table__table"]//tr')[1:]:
        if not e.find_elements(By.XPATH, './td[1]'): continue
        unit = e.find_element(By.XPATH, './td[1]').text[1:]
        rent = int(re.search(r'(\d+)', e.find_element(By.XPATH, './td[3]').text.replace(',', '')).group(1))
        totalRent = rent + fees
        rentPerArea = f'{totalRent / area:.2f}'
        printCsvLine(url, community, model, bedrooms, bathrooms, unit, area, rent, fees, totalRent, rentPerArea)


def crawl(driver: uc.Chrome):
    url = 'https://sonderyaustin.com/floorplans/'
    driver.get(url)
    urls = [e.get_attribute('href') \
            for e in driver.find_elements(By.XPATH, '//div[@class="skylease"]/ul/li/a')]
    for url in set(urls):
        crawlFloorplan(driver, url, 'Sondery', 70)