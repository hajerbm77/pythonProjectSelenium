from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.implicitly_wait(10)
driver.get('https://jqueryui.com/droppable/')
driver.implicitly_wait(10)

source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")

act_chain = ActionChains(driver)
act_chain.drag_and_drop(source, target).perform()

# act_chain.click_and_hold(source).move_to_element(target).release().perform()
# msg = driver.find_element(By.LINK_TEXT, 'Dropped!')
# try:
#     assert 'Dropped!' in msg
#     print('Test passed')
# except Exception as e:
#     print('Test failed')

driver.quit()
