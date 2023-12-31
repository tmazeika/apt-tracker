#!/usr/bin/env python3

import undetected_chromedriver as uc
from crawlers.alexan_riverside import AlexanRiversideCrawler
from crawlers.alexan_waterloo import AlexanWaterlooCrawler
from crawlers.camden_rainey import CamdenRaineyCrawler
from crawlers.corazon import CorazonCrawler
from crawlers.crawler import Crawler
from crawlers.skyhouse import SkyHouseCrawler
from crawlers.sondery import SonderyCrawler
from crawlers.windsor.windsor_eleven import WindsorElevenCrawler
from crawlers.windsor.windsor_on_the_lake import WindsorOnTheLakeCrawler
from crawlers.windsor.windsor_soco import WindsorSocoCrawler
from crawlers.windsor.windsor_south_lamar import WindsorSouthLamarCrawler

if __name__ == '__main__':
    options = uc.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-setuid-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1920,1080')
    driver = uc.Chrome(headless=True, use_subprocess=False, options=options)
    crawlers: list[Crawler] = [
        AlexanRiversideCrawler(driver),
        AlexanWaterlooCrawler(driver),
        WindsorElevenCrawler(driver),
        WindsorOnTheLakeCrawler(driver),
        WindsorSocoCrawler(driver),
        WindsorSouthLamarCrawler(driver),
        CamdenRaineyCrawler(driver),
        CorazonCrawler(driver),
        SkyHouseCrawler(driver),
        SonderyCrawler(driver),
    ]
    for crawler in crawlers:
        for unit in crawler.crawl():
            print(unit.json_dumps())