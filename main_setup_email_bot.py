from selenium_driverless.sync import webdriver
from selenium_driverless.types.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import os
import keyboard
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

EMAIL_ADDRESS = "Vittoriatryfeedbird@gmail.com"
PASSWORD = "Mintzyy@999"

RECOVERY_EMAIL_ADDRESS = "Stefan.weydt@gmail.com"
CAMPAIGN_NAME = "Edvin"

quickstart.main()
email_address_list = quickstart.getEmailList()
password_list = quickstart.getPasswordList()
index = quickstart.getLastIndex()
count = len(email_address_list)


for _ in range(count):
    driver = webdriver.Chrome()

    driver.get('http://accounts.google.com')
    driver.maximize_window()

    email_input = driver.find_element(By.CSS_SELECTOR, "input[type=\"email\"]", timeout=10)
    email_input.write(email_address_list[index])

    next_button = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button', timeout=10)
    next_button.click()
    sleep(3)
    try:
        password_input = driver.find_element(By.CSS_SELECTOR, "input[type=\"password\"]", timeout=10)
        password_input.write(password_list[index])

        next_button = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button', timeout=10)
        next_button.click()
    except:
        driver.quit()
        RANGE_NAME = f'Sheet1!C{index + 2}:C'
        quickstart.insertStatusInfo(RANGE_NAME, "Disabled")
        index += 1
        continue
    sleep(3)
    RANGE_NAME = f'Sheet1!C{index + 2}:C'
    quickstart.insertStatusInfo(RANGE_NAME, "Active")
    
    driver.get('https://myaccount.google.com/profile', wait_load=True)
    buttons = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/c-wiz[2]/c-wiz/div/div[2]/div/div/c-wiz/section/div[2]/div/div/div[3]/button', timeout=10)
    buttons.click()
    sleep(5)
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    print(len(iframes))
    iframe_document = iframes[1].content_document
    iframe_document.find_element(By.CSS_SELECTOR, "button[jsname=\"oKomv\"]", timeout=10).click()
    sleep(3)
    iframe_document.find_element(By.CSS_SELECTOR, "button[jsname=\"zf3vf\"]", timeout=10).click()
    sleep(3)
    iframe_document.find_element(By.CSS_SELECTOR, "button[jsname=\"NBieKd\"]", timeout=10).click()
    sleep(3)
    PHOTO_PATH = f"{getProjectPath.get_project_path()}\\photo\\{getRandomPhoto.get_random_photo()}"
    keyboard.write(PHOTO_PATH)
    sleep(1)
    press_tab_key(2)
    sleep(0.5)
    press_space_key()
    sleep(5)
    iframe_document.find_element(By.CSS_SELECTOR, "button[jsname=\"yTKzd\"]", timeout=10).click()
    sleep(2)
    iframe_document.find_element(By.CSS_SELECTOR, "button[jsname=\"WCwAu\"]", timeout=10).click()
    sleep(4)
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

    driver.get('https://mail.google.com/mail/u/0/#settings/accounts', wait_load=True)
    sleep(5)
    try:
        driver.switch_to.window(driver.window_handles[1])
    except:
        pass
    all_spans = driver.find_elements(By.TAG_NAME, "span")
    print(len(all_spans))
    for span in all_spans:
        if span.text == "edit info":
            span.click()
            break

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

    RANGE_NAME = f'Sheet1!D{index + 2}:D'
    quickstart.insertProfileStatus(RANGE_NAME, "Completed")

    sleep(3)
    driver.quit()

    axios_newsletter_subscribe_bot.run_subscribe_bot(email_address_list[index])
    RANGE_NAME = f'Sheet1!E{index + 2}:G'
    quickstart.insertSubscriptionStatus(RANGE_NAME, "Completed", "", "Completed")

    sleep(3)
    index += 1
    