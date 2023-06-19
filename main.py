#!/usr/bin/env python3

import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from util import printUnitInfo
from alexan_riverside import crawl as crawlAlexanRiverside
from sondery import crawl as crawlSondery
from windsor_eleven import crawl as crawlEleven
from windsor_monarch import crawl as crawlMonarch
from windsor_on_the_lake import crawl as crawlWindsorOnTheLake
from windsor_soco import crawl as crawlSoco
from windsor_south_lamar import crawl as crawlWindsorSouthLamar

if __name__ == '__main__':
    options = uc.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-setuid-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--start-maximized")
    options.add_argument("--window-size=1920,1080")
    driver = uc.Chrome(headless=True, use_subprocess=False, options=options)
    crawlAlexanRiverside(driver)
    crawlSondery(driver)
    crawlEleven(driver)
    crawlMonarch(driver)
    crawlWindsorOnTheLake(driver)
    crawlSoco(driver)
    crawlWindsorSouthLamar(driver)