from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from time import sleep


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=C:/Users/Administrator/AppData/Local/Google/Chrome/User Data")
chrome_options.add_argument('--profile-directory=Default')  # Replace with the actual Chrome profile directory

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get("https://myaccount.google.com/profile")

buttons = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/c-wiz[2]/c-wiz/div/div[2]/div/div/c-wiz/section/div[2]/div/div/div[3]/button')
buttons.click()


driver.switch_to.frame(1)

modal = driver.find_element(By.CSS_SELECTOR, "c-wiz[class=\"zGzCU ftAIlf wiax5e WjBoXb rqSEqc SSPGKf TJKThb gt34yd\"]")
button = modal.find_element(By.CSS_SELECTOR, "button[class=\"VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-INsAgc VfPpkd-LgbsSe-OWXEXe-Bz112c-M1Soyc VfPpkd-LgbsSe-OWXEXe-dgl2Hf Rj2Mlf OLiIxf PDpWxe LQeN7 Yt8mjf\"]")
button.click()