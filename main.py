#!/usr/bin/env python3

import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from util import printCsvLine
from alexan_riverside import crawl as crawlAlexanRiverside
from sondery import crawl as crawlSondery
from windsor_eleven import crawl as crawlEleven
from windsor_monarch import crawl as crawlMonarch
from windsor_on_the_lake import crawl as crawlWindsorOnTheLake
from windsor_soco import crawl as crawlSoco
from windsor_south_lamar import crawl as crawlWindsorSouthLamar

if __name__ == '__main__':
    printCsvLine("URL", "Community", "Model", "Bedrooms", "Bathrooms", "Unit", "Area (sqft)", "Rent ($)", "Fees ($)", "Total Rent ($)", "$/sqft")
    driver = uc.Chrome(headless=True, use_subprocess=False)
    crawlAlexanRiverside(driver)
    crawlSondery(driver)
    crawlEleven(driver)
    crawlMonarch(driver)
    crawlWindsorOnTheLake(driver)
    crawlSoco(driver)
    crawlWindsorSouthLamar(driver)