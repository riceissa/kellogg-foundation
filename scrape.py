#!/usr/bin/env python3

from selenium import webdriver
import time
import sys

LAST_PAGE = 202
DIRECTORY = sys.argv[1]

for page in range(1, LAST_PAGE + 1):
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    url = f"https://www.wkkf.org/grants#pp=100&p={page}"
    driver.get(url)
    time.sleep(5)
    html = driver.execute_script("return document.documentElement.outerHTML")
    driver.quit()
    with open(DIRECTORY + f"/page-{page}.html", "w") as f:
        f.write(html)
