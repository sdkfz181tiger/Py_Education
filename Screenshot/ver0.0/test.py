#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHROME_BIN = "/usr/bin/chromium-browser"
CHROME_DRIVER = '/usr/bin/chromedriver'

options = Options()
options.binary_location = CHROME_BIN
options.add_argument('--headless')
options.add_argument('--window-size=1280,1080')

driver = webdriver.Chrome(CHROME_DRIVER, options=options)

driver.get("https://www.google.co.jp")
time.sleep(5)# Sleep
driver.save_screenshot("./test.png")
driver.quit()