from selenium import webdriver
from selenium_driverless.sync import webdriver as driverless_webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

EMAIL_ADDRESS = "Alfietryffeedbirrdz@gmail.com"
PASSWORD = "Siraj@333"
# Set the path to the directory where you want to create the profile
profile_directory = 'C:/Profile 1236'

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--user-data-dir=' + profile_directory)
# Create a new Chrome driver with the specified options
create_profile_driver = webdriver.Chrome(options=chrome_options)

# Open any website to initialize the profile
create_profile_driver.get('https://accounts.google.com')
# At this point, the new profile has been created and initialized.
# You can customize the profile further or use it for your specific needs.
create_profile_driver.quit()

###########################################################
driverless_options = driverless_webdriver.ChromeOptions()
driverless_options.add_argument('--user-data-dir=' + profile_directory)
# Create a new Chrome driver with the specified options
driverless_driver = driverless_webdriver.Chrome(options=driverless_options)

driverless_driver.get('http://accounts.google.com')

WebDriverWait(driverless_driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"email\"]")))
email_input = driverless_driver.find_element(By.CSS_SELECTOR, "input[type=\"email\"]")
email_input.write(EMAIL_ADDRESS)

next_button = driverless_driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button')
next_button.click()

sleep(3)

password_input = driverless_driver.find_element(By.CSS_SELECTOR, "input[type=\"password\"]")
password_input.write(PASSWORD)

next_button = driverless_driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button')
next_button.click()
sleep(3)
###########################################################

try:
    driver = webdriver.Chrome(options=chrome_options)
    # Open any website to initialize the profile
    driver.get('https://accounts.google.com')
except:
    driverless_driver.quit()
    driver.quit()

# driverless_driver.quit()
# driver = webdriver.Chrome(options=chrome_options)
    # Open any website to initialize the profile
    # driver.get('https://accounts.google.com')

sleep(1000)

