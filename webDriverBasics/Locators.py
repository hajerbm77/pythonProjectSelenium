from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(20)
driver.get('https:classic.crmpro.com/')
# print(driver.title)

# features = driver.find_element(By.PARTIAL_LINK_TEXT, 'Features')
# features.click()
# print(driver.title)
# driver.back()
# driver.find_element(By.CLASS_NAME, "navbar-brand")
# username = driver.find_element(By.NAME, 'username')
# password = driver.find_element(By.NAME, 'password')
# login_btn = driver.find_element(By.XPATH, "//input[@type='submit']")
# username.send_keys('tester')
# password.send_keys('Tester123')
# login_btn.click()

# services = driver.find_elements(By.CSS_SELECTOR, '#navbar-collapse li a')
#
# for ele in services:  #click on Pricing
#     if ele.text == 'Pricing':
#         ele.click()
#         break
# driver.find_element(By.CLASS_NAME, 'active').click()

# driver.find_element(By.LINK_TEXT, 'Sign Up').click()  # when 'a' tag is available
# driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign').click()  # when 'a' tag is available
# header_element = driver.find_element(By.TAG_NAME, 'h1')
# print(header_element.text)

linkList = driver.find_elements(By.TAG_NAME, 'a')
print(len(linkList))

for ele in linkList:
    link_text = ele.text
    print(link_text)
    print(ele.get_attribute('href'))  # for navigation

imageList = driver.find_elements(By.TAG_NAME, 'img')
print(len(imageList))
for ele in imageList:
    print(ele.get_attribute('src'))  # src where it is coming





# time.sleep(10)

driver.quit()
