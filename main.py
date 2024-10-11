from selenium_driverless.sync import webdriver
from selenium_driverless.types.by import By
from time import sleep
import newletter_verification
import quickstart
import axios_newsletter_subscribe_bot

quickstart.main()
accountList = quickstart.getAccountList()
proxyList = quickstart.getProxyList()

passwordToChangeList = quickstart.getPasswordToChangeList()

anotherAccountList = quickstart.getAnotherAccountList()
anotherProxyList = quickstart.getAnotherProxyList()

aliasList = quickstart.getAliasList()

index = quickstart.getLastIndex()
count = len(accountList)

num = count - index
for _ in range(num):

    # EMAIL_ADDRESS = "pkmnbvcxsryjhcdf876@gmail.com"
    # PASSWORD = "DFJSDFJ#$*#(ksdjf234JDFHDF)"
    # RECOVERY_EMAIL_ADDRESS = "pkmnbvcxsryjhcdf87617@outlook.com"

    # PASSWORD_TO_CHANGE = "DFJSDFJ#$*#(ksdjf234JDFHDF)"

    # ALIAS = "zajan"
    # ANOTHER_EMAIL_ADDRESS = "yhebevsjskifshbdjdi@gmail.com"
    # ANOTHER_EMAIL_PASSWORD = "A9dK2tFrYf8k"
    # ANOTHER_EMAIL_RECOVERY = "yhebevsjskifshbdjdi81@outlook.com"
    
    EMAIL_ADDRESS = accountList[index].split(":")[0]
    PASSWORD = accountList[index].split(":")[1]
    RECOVERY_EMAIL_ADDRESS = accountList[index].split(":")[2]

    PASSWORD_TO_CHANGE = passwordToChangeList[index]

    ALIAS = aliasList[index]
    ANOTHER_EMAIL_ADDRESS = anotherAccountList[index].split(":")[0]
    ANOTHER_EMAIL_PASSWORD = anotherAccountList[index].split(":")[0]
    ANOTHER_EMAIL_RECOVERY = anotherAccountList[index].split(":")[0]

    axios_newsletter_subscribe_bot.run_subscribe_bot(EMAIL_ADDRESS)
    RANGE_NAME = f'email warm up!D{index + 2}:D'
    quickstart.insertInfo(RANGE_NAME, "done")


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
        RANGE_NAME = f'email warm up!C{index + 2}:C'
        quickstart.insertInfo(RANGE_NAME, "Disabled")
        index += 1
        continue
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
    RANGE_NAME = f'email warm up!C{index + 2}:C'
    quickstart.insertInfo(RANGE_NAME, "Active")
    sleep(5)
    driver.get("https://mail.google.com/mail/u/0/#search/action+required+%3A+confirm+your+axios+subscription", wait_load=True)
    sleep(5)
    spans = driver.find_elements(By.CSS_SELECTOR, "span[class=\"il\"]")
    print(len(spans))
    for span in spans:
        if "Action" in span.text:
            span.click()
            break
    sleep(5)

    verify_email_link = ""
    a_links = driver.find_elements(By.TAG_NAME, "a")
    print(len(a_links))
    for a_link in a_links:
        if "verify email" in a_link.text.lower():
            verify_email_link = driver.execute_script("return arguments[0].getAttribute('href');", a_link)
            print(verify_email_link)
            break

    newletter_verification.verification(verifylink=verify_email_link)

    RANGE_NAME = f'email warm up!E{index + 2}:E'
    quickstart.insertInfo(RANGE_NAME, "done")

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



    name_input = driver.find_element(By.CSS_SELECTOR, "input[aria-labelledby=\"nameLabel\"]")
    name_input.clear()
    name_input.write(ALIAS)

    another_email_input = driver.find_element(By.CSS_SELECTOR, "input[id=\"focus\"]")
    another_email_input.write(ANOTHER_EMAIL_ADDRESS)

    next_step_button = driver.find_element(By.CSS_SELECTOR, "input[type=\"submit\"]")
    next_step_button.click()
    sleep(2)
    while True:
        try:
            send_verification_button = driver.find_element(By.CSS_SELECTOR, "input[value=\"Send Verification\"]")
            send_verification_button.click()
            break
        except:
            sleep(3)
            pass

    sleep(5)
    driver.find_element(By.CSS_SELECTOR, "a[id=\"cancel\"]").click()
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()

    another_driver = webdriver.Chrome()
    another_driver.maximize_window()
    another_driver.get("https://mail.google.com/mail/u/0/#search/Gmail+Confirmation+-+Send+Mail+as", wait_load=True)

    sleep(3)
    email_input = another_driver.find_element(By.CSS_SELECTOR, "input[type=\"email\"]")
    email_input.write(ANOTHER_EMAIL_ADDRESS)

    next_button = another_driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button')
    next_button.click()

    sleep(3)
    try:
        password_input = another_driver.find_element(By.CSS_SELECTOR, "input[type=\"password\"]")
        password_input.write(ANOTHER_EMAIL_PASSWORD)

        next_button = another_driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button')
        next_button.click()
    except:
        another_driver.quit()
        RANGE_NAME = f'email warm up!J{index + 2}:J'
        quickstart.insertInfo(RANGE_NAME, "Disabled")
        index += 1
        continue
    try:
        sleep(5)
        challenges = another_driver.find_elements(By.CSS_SELECTOR, "div[class=\"l5PPKe\"]")
        print(len(challenges))
        for challenge in challenges:
            if "Confirm your recovery email" in challenge.text:
                challenge.click()
                break
        sleep(3)
        recovery_email_input = another_driver.find_element(By.CSS_SELECTOR, "input[type=\"email\"]")
        recovery_email_input.write(ANOTHER_EMAIL_RECOVERY)
        next_button = another_driver.find_elements(By.CSS_SELECTOR, "button[type=\"button\"]")[0]
        next_button.click()
    except:
        pass
    RANGE_NAME = f'email warm up!J{index + 2}:J'
    quickstart.insertInfo(RANGE_NAME, "Active")
    sleep(5)
    another_driver.get("https://mail.google.com/mail/u/0/#search/Gmail+Confirmation+-+Send+Mail+as", wait_load=True)
    sleep(5)
    spans = another_driver.find_elements(By.CSS_SELECTOR, "span[class=\"il\"]")
    print(len(spans))
    for span in spans:
        if "Confirmation" in span.text:
            span.click()
            break
    sleep(5)

    verify_link = ""
    a_links = another_driver.find_elements(By.CSS_SELECTOR, "a[rel=\"noreferrer\"]")
    print(len(a_links))
    verify_link = another_driver.execute_script("return arguments[0].getAttribute('href');", a_links[0])
    print(verify_link)

    another_driver.get(verify_link, wait_load=True)
    sleep(3)
    confirm_button = another_driver.find_element(By.CSS_SELECTOR, "input[value=\"Confirm\"][type=\"submit\"]")
    confirm_button.click()
    sleep(2)
    another_driver.quit()

    driver.refresh()
    sleep(5)
    spans = driver.find_elements(By.TAG_NAME, "span")
    for span in spans:
        if "make default" in span.text:
            span.click()
            break
    sleep(2)

    RANGE_NAME = f'email warm up!L{index + 2}:L'
    quickstart.insertInfo(RANGE_NAME, "done")

    driver.get("https://myaccount.google.com/security?utm_source=chrome-profile-chooser", wait_load=True)
    sleep(3)
    password_change_element = driver.find_element(By.CSS_SELECTOR, "a[aria-label=\"Password\"]")
    link = driver.execute_script("return arguments[0].getAttribute('href');", password_change_element)
    if "https://myaccount.google.com" not in link:
        link = f"https://myaccount.google.com/{link}"
    print(link)

    driver.get(link, wait_load=True)
    sleep(5)
    new_password_input = driver.find_element(By.CSS_SELECTOR, "input[name=\"password\"]")
    new_password_input.write(PASSWORD_TO_CHANGE)

    confirm_password_input = driver.find_element(By.CSS_SELECTOR, "input[name=\"confirmation_password\"]")
    confirm_password_input.write(PASSWORD_TO_CHANGE)

    spans = driver.find_elements(By.TAG_NAME, "span")
    for span in spans:
        if "Change password" in span.text:
            span.click()
            break

    sleep(5)
    RANGE_NAME = f'email warm up!G{index + 2}:G'
    quickstart.insertInfo(RANGE_NAME, "done")
    driver.quit()

    index += 1