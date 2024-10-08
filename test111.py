from selenium_driverless.sync import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import os
import keyboard
import pyautogui
import getProjectPath
import getRandomPhoto
import axios_newsletter_subscribe_bot
import quickstart

def press_tab_key(count):
    for _ in range(count):
        keyboard.press('tab')
        keyboard.release('tab')
def press_space_key():
    keyboard.press('space')
    keyboard.release('space')

EMAIL_ADDRESS = "Alfietryffeedbirrdz@gmail.com"
PASSWORD = "Siraj@333"

RECOVERY_EMAIL_ADDRESS = "Stefan.weydt@gmail.com"
CAMPAIGN_NAME = "Edvin"

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

driver.get('http://accounts.google.com')
driver.maximize_window()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"email\"]")))
email_input = driver.find_element(By.CSS_SELECTOR, "input[type=\"email\"]")
email_input.write(EMAIL_ADDRESS)

next_button = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button')
next_button.click()

sleep(3)
password_input = driver.find_element(By.CSS_SELECTOR, "input[type=\"password\"]")
password_input.write(PASSWORD)

next_button = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button')
next_button.click()

sleep(3)
driver.get('https://myaccount.google.com/profile')
sleep(3)
buttons = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/c-wiz[2]/c-wiz/div/div[2]/div/div/c-wiz/section/div[2]/div/div/div[3]/button')
buttons.click()

driver.switch_to.frame(1)
sleep(3)
modal = driver.find_element(By.CSS_SELECTOR, "c-wiz[class=\"zGzCU ftAIlf wiax5e WjBoXb rqSEqc SSPGKf TJKThb gt34yd\"]")
button = modal.find_element(By.CSS_SELECTOR, "button[class=\"VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-INsAgc VfPpkd-LgbsSe-OWXEXe-Bz112c-M1Soyc VfPpkd-LgbsSe-OWXEXe-dgl2Hf Rj2Mlf OLiIxf PDpWxe LQeN7 Yt8mjf\"]")
button.click()

sleep(3)
press_tab_key(6)
sleep(2)
press_space_key()
sleep(5)
screen_width, screen_height = pyautogui.size()
# Specify the pixel point where you want to click
x = screen_width / 2 + 10
y = screen_height / 4.9
# Perform a mouse click at the specified pixel point
pyautogui.click(x, y)
sleep(2)
press_tab_key(1)
sleep(0.5)
press_space_key()
sleep(1)
PHOTO_PATH = f"{getProjectPath.get_project_path()}\\photo\\{getRandomPhoto.get_random_photo()}"
keyboard.write(PHOTO_PATH)
sleep(1)
press_tab_key(2)
sleep(0.5)
press_space_key()
sleep(5)
press_tab_key(9)
sleep(0.5)
press_space_key()
sleep(5)
press_space_key()
sleep(4)
press_tab_key(1)
press_space_key()
sleep(2)
#########################################################################################
# driver.get('https://myaccount.google.com/security')
# sleep(3)

# recovery_email_button = driver.find_element(By.CSS_SELECTOR, "a[aria-label=\"Recovery email\"]")
# recovery_email_button.click()
# sleep(3)
# recovery_email_input = driver.find_element(By.CSS_SELECTOR, "input[type=\"email\"]")
# recovery_email_input.write(RECOVERY_EMAIL_ADDRESS)

# next_button = driver.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]")
# next_button.click()

driver.get('https://mail.google.com/mail/u/0/#settings/accounts')
sleep(5)
try:
    driver.switch_to.window(driver.window_handles[1])
except:
    pass
sleep(2)
press_tab_key(15)
keyboard.press('enter')
keyboard.release('enter')
sleep(3)
print(driver.current_url)
driver.switch_to.window(driver.window_handles[1])
print(driver.current_url)
sleep(2)
driver.switch_to.window(driver.window_handles[0])
print(driver.current_url)
sleep(2)
# name_input = driver.find_element(By.CSS_SELECTOR, "input[id=\"cfn\"]")
# name_input.write(CAMPAIGN_NAME)
press_tab_key(2)
sleep(0.5)
keyboard.write(CAMPAIGN_NAME)

# driver.switch_to.window(driver.window_handles[1])
sleep(1)
reply_to_address_link = driver.find_element(By.CSS_SELECTOR, "span[id=\"diff_reply_to\"]")
reply_to_address_link.click()
sleep(2)
reply_to_address_input = driver.find_element(By.CSS_SELECTOR, "input[id=\"cfrt\"]")
reply_to_address_input.write(RECOVERY_EMAIL_ADDRESS)
sleep(1)
save_changes_button = driver.find_element(By.CSS_SELECTOR, "input[type=\"submit\"]")
save_changes_button.click()

if os.path.exists(PHOTO_PATH):
    # Delete the file
    os.remove(PHOTO_PATH)
    print("File deleted successfully.")
else:
    print("File does not exist.")


sleep(3)
driver.quit()



sleep(3)
    