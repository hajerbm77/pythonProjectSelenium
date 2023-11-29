from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait((10))
driver.get('https://www.orangehrm.com/orangehrm-30-day-trial')

ele_country = driver.find_element(By.ID, "Form_getForm_Country")
select = Select(ele_country)

#select.select_by_visible_text('Tunisia')
#select.select_by_index(3) #make sure to remember that index starts at 0
#select.select_by_value('France') #this is the tag

#print(select.is_multiple)  #meaning is it yes or no a multiple select (can I choose more than one?)

# def select_values(element, value): #if more than more dropdown it is better to create a method
#     select = Select(element)
#     select.select_by_visible_text(value)
# ele_country = driver.find_element(By.ID, "Form_getForm_Country")
# ele_city = driver.find_element(By.ID, "Form_getForm_City")  #not in the website!!
#
# select_values('France', 'Paris')

# select = Select(ele_country)
# country_list = select.options
#
# for ele in country_list:
#     print(ele.text)
#     if ele.text == 'Tunisia':
#         ele.click()
#         break

# country_list = driver.find_elements(By.XPATH, '//select[@id="Form_getForm_Country"]/option')  # without Select
# for ele in country_list:
#     print(ele.text)
#     if ele.text == 'Germany':
#         ele.click()
#         break

country_list = driver.find_elements(By.XPATH, '//select[@id="Form_getForm_Country"]/option')
def select_values_from_dropdown(dropdownList, value):  #same thig we can create a generic method without select
    for ele in country_list:
        print(ele.text)
        if ele.text == value:
            ele.click()
            break
select_values_from_dropdown(country_list, 'Portugal')


time.sleep(10)
driver.quit()
