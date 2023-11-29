from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

# def select_values(options_list, value):# for single or multiple choices
#     for ele in options_list:
#         print(ele.text)
#         if ele.text == value:
#             ele.click()
#             break

# def select_values(options_list, value): # single or more choices
#     for ele in options_list:
#         print(ele.text)
#         for k in range(len(value)):
#             if ele.text == value[k]:
#                 ele.click()
#                 break

def select_values(options_list, value): # for ALL choices
    if not value[0] == 'all':
        for ele in options_list:
            print(ele.text)
            for k in range(len(value)):
                if ele.text == value[k]:
                    ele.click()
                    break
    else:
        try:
            for ele in options_list:
                ele.click()
        except Exception as e:
            print(e)



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait((10))
driver.get('https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/')
driver.find_element(By.ID, 'justAnInputBox').click()
dropDownList = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle ')

values_list = ['choice 1', 'choice 2', 'choice 6 2 1'] #multiple choices
# select_values(dropDownList, values_list)#multiple choices in a list

# select_values(dropDownList, 'choice 2') #single choice
# select_values(dropDownList, 'choice 5')

# values_list = ['all'] #testing our code is valid with all choices
# values_list = ['choice 7']  #testing our code is valid with last option in the list
select_values(dropDownList, values_list)

# for ele in dropDownList:  #single choice
#     print(ele.text)
#     if ele.text == 'choice 6 2 3':
#         ele.click()
#         break

time.sleep(10)
driver.quit()