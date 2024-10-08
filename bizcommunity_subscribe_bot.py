from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import random_name_generator

def scroll_down(driv):
    page_height = driv.execute_script("return document.body.scrollHeight")
    scroll_distance = page_height // 5
    driv.execute_script(f"window.scrollTo(0, {scroll_distance});")
    sleep(0.3)
    driv.execute_script(f"window.scrollTo({scroll_distance}, {scroll_distance * 2});")
    sleep(0.3)
    driv.execute_script(f"window.scrollTo({scroll_distance * 2}, {scroll_distance * 3});")
    sleep(0.3)
    driv.execute_script(f"window.scrollTo({scroll_distance * 3}, {scroll_distance * 4});")
    sleep(0.3)
    driv.execute_script(f"window.scrollTo({scroll_distance * 4}, {page_height});")

def run_bot(driver, email_address):
    # email_addresses = [
    #     'randomuser1@example.com',
    #     'email1234@gmail.com',
    #     'testmail@hotmail.com',
    #     'user4321@yahoo.com',
    #     'sampleemail@outlook.com',
    #     'randomemail5678@gmail.com',
    #     'myemailaddress@yahoo.com',
    #     'examplemail4567@outlook.com',
    #     'useremail123@hotmail.com',
    #     'testuser9876@gmail.com'
    # ]
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("user-data-dir=C:/Users/Administrator/AppData/Local/Google/Chrome/User Data")
    # chrome_options.add_argument('--profile-directory=Default')  # Replace with the actual Chrome profile directory

    # driver = webdriver.Chrome(options=chrome_options)
    # driver.maximize_window()
    driver.get("https://www.bizcommunity.com/Signup.aspx")
    sleep(2)
    save_button = driver.find_element(By.CSS_SELECTOR, "input[id=\"xSubmit\"]")
    driver.execute_script("arguments[0].scrollIntoView();", save_button)
    sleep(15)
    scroll_down(driver)

    email_input = driver.find_element(By.CSS_SELECTOR, "input[id=\"xEmailAddress\"]")
    email_input.send_keys(email_address)

    first_name, last_name = random_name_generator.random_name()
    print(first_name, last_name)
    first_name_input = driver.find_element(By.CSS_SELECTOR, "input[id=\"xFirstName\"]")
    first_name_input.send_keys(first_name)
    last_name_input = driver.find_element(By.CSS_SELECTOR, "input[id=\"xLastName\"]")
    last_name_input.send_keys(last_name)

    check_box_elements = driver.find_elements(By.CSS_SELECTOR, "input[type=\"checkbox\"]")
    check_box_elements = check_box_elements[1:-2]
    print(len(check_box_elements))

    actions = ActionChains(driver)

    # Perform the click action
    for check_box in check_box_elements:
        actions.click(check_box).perform()

    save_button = driver.find_element(By.CSS_SELECTOR, "input[id=\"xSubmit\"]")
    save_button.click()
    sleep(2)
