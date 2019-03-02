#!/usr/bin/env python2

from selenium import webdriver

driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.CHROME.copy())
driver.get("https://docs.seleniumhq.org")
print "page title=" + driver.title
