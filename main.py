#!/usr/bin/env python3

import undetected_chromedriver as uc
from crawlers.alexan.alexan_riverside import AlexanRiversideCrawler
from crawlers.crawler import Crawler
from crawlers.skyhouse import SkyHouseCrawler
from crawlers.sondery import SonderyCrawler
from crawlers.windsor.windsor_eleven import WindsorElevenCrawler
from crawlers.windsor.windsor_monarch import WindsorMonarchCrawler
from crawlers.windsor.windsor_on_the_lake import WindsorOnTheLakeCrawler
from crawlers.windsor.windsor_soco import WindsorSocoCrawler
from crawlers.windsor.windsor_south_lamar import WindsorSouthLamarCrawler

if __name__ == '__main__':
    options = uc.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-setuid-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--start-maximized")
    options.add_argument("--window-size=1920,1080")
    driver = uc.Chrome(headless=True, use_subprocess=False, options=options)
    driver.set_page_load_timeout(30)
    crawlers: list[Crawler] = [
        AlexanRiversideCrawler(driver),
        WindsorElevenCrawler(driver),
        WindsorMonarchCrawler(driver),
        WindsorOnTheLakeCrawler(driver),
        WindsorSocoCrawler(driver),
        WindsorSouthLamarCrawler(driver),
        SkyHouseCrawler(driver),
        SonderyCrawler(driver),
    ]
    for crawler in crawlers:
        for unit in crawler.crawl():
            print(unit.json_dumps())