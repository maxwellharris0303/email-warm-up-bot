from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep

email_addresses = [
    'randomuser1@example.com',
    'email1234@gmail.com',
    'testmail@hotmail.com',
    'user4321@yahoo.com',
    'sampleemail@outlook.com',
    'randomemail5678@gmail.com',
    'myemailaddress@yahoo.com',
    'examplemail4567@outlook.com',
    'useremail123@hotmail.com',
    'testuser9876@gmail.com'
]
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=C:/Users/Administrator/AppData/Local/Google/Chrome/User Data")
chrome_options.add_argument('--profile-directory=Default')  # Replace with the actual Chrome profile directory

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get("https://www.buzzfeed.com/newsletters")
sleep(2)

for email in email_addresses:
    input_email = driver.find_element(By.CSS_SELECTOR, "input[data-testid=\"email-input\"]")
    input_email.clear()
    input_email.send_keys(email)

    check_box_elements = driver.find_elements(By.CSS_SELECTOR, "label[class=\"newsletter-item_newsletterTitle__SxheF\"]")
    print(len(check_box_elements))

    for check_box in check_box_elements:
        check_box.click()

    sign_up_button = driver.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]")
    sign_up_button.click()

    page_height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script(f"window.scrollTo({page_height}, 0);")
    sleep(5)
