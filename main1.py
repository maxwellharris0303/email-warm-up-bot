import undetected_chromedriver as uc
driver = uc.Chrome(headless=True,use_subprocess=False)
driver.get('https://nowsecure.nl')
driver.save_screenshot('nowsecure.png')