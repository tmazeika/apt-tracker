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
    driver = uc.Chrome(headless=True, use_subprocess=False)
    driver.set_page_load_timeout(10)
    driver.implicitly_wait(10)
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
    try:
        for crawler in crawlers:
            for unit in crawler.crawl():
                print(unit.json_dumps())
    except:
        driver.save_screenshot('error.png')
        raise