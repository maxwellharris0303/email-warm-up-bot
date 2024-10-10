from selenium_driverless.sync import webdriver
from selenium_driverless.types.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
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
    profile_directory = 'C:/Profile newsletter'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f'--user-data-dir={profile_directory}')

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    driver.get("https://www.axios.com/newsletters")
    sleep(2)
    while True:
        try:
            driver.find_element(By.CSS_SELECTOR, "div[class=\"p-1.5 border border-accent-blue-core rounded-3xl relative focus-within:outline focus-within:outline-accent-blue-core\"]")
            break
        except:
            sleep(0.3)

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
    flag = False
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
            if index == 5:
                flag = True
                break
        if flag:
            break


    email_input = driver.find_element(By.CSS_SELECTOR, "input[data-cy=\"newsletter-email-input\"]")
    email_input.write(email_address)
    subscribe_button = driver.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]")
    subscribe_button.click()
    sleep(3)
    # try:
    #     WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[class=\"text-error\"]")))
    #     print("Wrong Email Address")
    # except:
    #     print("NExt ACTION")
    # bizcommunity_subscribe_bot.run_bot(driver, email_address)

    driver.quit()

# run_subscribe_bot("sdfsdf@gmail.com")

