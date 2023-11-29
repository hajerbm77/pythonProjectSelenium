from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(20)
driver.get('https://the-internet.herokuapp.com/jqueryui/menu')

enabled_ele = driver.find_element(By.ID, 'ui-id-3')
act_chains = ActionChains(driver)
act_chains.move_to_element(enabled_ele).perform()

back_query_ele = driver.find_element(By.ID, 'ui-id-8')
back_query_ele.click()
try:
    assert 'The Internet' in driver.title
    print('Assertion pass')
except Exception as e:
    print('Assertion test failed, format(e')

time.sleep(3)

driver.quit()
