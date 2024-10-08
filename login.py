from selenium_driverless.sync import webdriver
from selenium_driverless.types.by import By
from time import sleep

EMAIL_ADDRESS = "pkmnbvcxsryjhcdf876@gmail.com"
PASSWORD = "9fdNhFEeICw9ke7i"
RECOVERY_EMAIL_ADDRESS = "pkmnbvcxsryjhcdf87617@outlook.com"

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get("https://accounts.google.com", wait_load=True)
sleep(3)
email_input = driver.find_element(By.CSS_SELECTOR, "input[type=\"email\"]")
email_input.write(EMAIL_ADDRESS)

next_button = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button')
next_button.click()

sleep(3)
try:
    password_input = driver.find_element(By.CSS_SELECTOR, "input[type=\"password\"]")
    password_input.write(PASSWORD)

    next_button = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button')
    next_button.click()
except:
    driver.quit()
    # RANGE_NAME = f'Sheet1!D{index + 2}:D'
    # quickstart.insertStatusInfo(RANGE_NAME, "Disabled")
    # index += 1
    # continue
try:
    sleep(5)
    challenges = driver.find_elements(By.CSS_SELECTOR, "div[class=\"l5PPKe\"]")
    print(len(challenges))
    for challenge in challenges:
        if "Confirm your recovery email" in challenge.text:
            challenge.click()
            break
    sleep(3)
    recovery_email_input = driver.find_element(By.CSS_SELECTOR, "input[type=\"email\"]")
    recovery_email_input.write(RECOVERY_EMAIL_ADDRESS)
    next_button = driver.find_elements(By.CSS_SELECTOR, "button[type=\"button\"]")[0]
    next_button.click()
except:
    pass

driver.get("https://mail.google.com/mail/u/0/#settings/accounts", wait_load=True)
sleep(3)

spans = driver.find_elements(By.TAG_NAME, "span")
for span in spans:
    if "Add another email address" in span.text:
        span.click()
        break
sleep(3)
windows = driver.window_handles
for window in windows:
    if "Add another email address you own" in str(window):
        print("Add another email address you own")
        driver.switch_to.window(window)
        print(driver.current_url)