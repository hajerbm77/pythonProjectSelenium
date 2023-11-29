import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
print(driver.title)
# time.sleep(20)
driver.find_element(By.NAME,'q').send_keys("dress shoes")
options = driver.find_elements(By.CSS_SELECTOR,'div.wM6W7d span')
print(len(options))

for ele in options:
    # print(ele.text)
    if ele.text == 'dress shoes for women':
        ele.click()
        break

time.sleep(5)
driver.quit()