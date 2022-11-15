# https://www.youtube.com/watch?v=gCWSdpLepHM&ab_channel=ThePylot

from time import sleep
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

sleep(5)

driver = webdriver.Remote('https://selenium:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)

driver.get('https://python.org')
driver.save_screenshot('screenshot.png')