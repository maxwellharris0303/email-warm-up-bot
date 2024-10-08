from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from time import sleep
import bizcommunity_subscribe_bot

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

def run_subscribe_bot(email_address):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("user-data-dir=C:/Users/Administrator/AppData/Local/Google/Chrome/User Data")
    chrome_options.add_argument('--profile-directory=Default')  # Replace with the actual Chrome profile directory

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    driver.get("https://www.axios.com/newsletters")
    sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"p-1.5 border border-accent-blue-core rounded-3xl relative focus-within:outline focus-within:outline-accent-blue-core\"]")))

    next_card_buttons = driver.find_elements(By.CSS_SELECTOR, "button[aria-label=\"Next slide\"]")

    card_parents = []
    card_parents.extend(driver.find_elements(By.CSS_SELECTOR, "div[class=\"swiper swiper-initialized swiper-horizontal swiper-backface-hidden\"]"))
    card_parents.extend(driver.find_elements(By.CSS_SELECTOR, "div[class=\"swiper swiper-initialized swiper-horizontal\"]"))
    print(len(card_parents))

    next_card_buttons = []
    for card_parent in card_parents:
        next_card_button_parent = card_parent.find_element(By.XPATH, "..")
        next_card_buttons.append(next_card_button_parent.find_element(By.CSS_SELECTOR, "button[aria-label=\"Next slide\"]"))
    print(len(next_card_buttons))

    index = 0
    for card_parent in card_parents:
        card_elements = card_parent.find_elements(By.CSS_SELECTOR, "div[class=\"p-1.5 border border-accent-blue-core rounded-3xl relative focus-within:outline focus-within:outline-accent-blue-core\"]")
        print(len(card_elements))
        for card_element in card_elements:
            try:
                card_element.click()
            except:
                next_card_buttons[index].click()
                sleep(0.5)
                card_element.click()
        index += 1


    email_input = driver.find_element(By.CSS_SELECTOR, "input[data-cy=\"newsletter-email-input\"]")
    email_input.send_keys(email_address)
    email_input.send_keys(Keys.RETURN)
    sleep(3)
    # try:
    #     WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[class=\"text-error\"]")))
    #     print("Wrong Email Address")
    # except:
    #     print("NExt ACTION")
    bizcommunity_subscribe_bot.run_bot(driver, email_address)

    driver.quit()

