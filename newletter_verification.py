from selenium_driverless.sync import webdriver
from selenium_driverless.types.by import By
from time import sleep

def verification(verifylink):
    driver = webdriver.Chrome()
    driver.get(verifylink)
    sleep(3)
    driver.quit()