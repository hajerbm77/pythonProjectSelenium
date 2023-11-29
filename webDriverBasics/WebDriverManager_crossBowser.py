# selenium 4
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.safari import service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

name = "opera"
if name == 'chrome':
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

elif name == 'edge':
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

elif name == 'firefox':
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
else:
    print(" Pass the correct browser name: " + name)
    raise Exception('driver is not found')

driver.implicitly_wait(6)
driver.get('https://app.hubspot.com/login')
driver.find_element(By.ID,"username").send_keys('tester')
driver.find_element(By.ID,"password").send_keys('Test123')
driver.find_element(By.ID,'loginBtn').click()

print(driver.title)

driver.quit()



