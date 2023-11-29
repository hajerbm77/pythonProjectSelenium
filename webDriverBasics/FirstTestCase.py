# Open web browser (chrome/ firefox/ Edge)
# Open URL https://opensource-demo.orangehrmlive.com
# Provide email (admin@yourstore.com)
# Provide password (admin)
# Click login
# Capture title of dashboard page (actual title)
# Verify title  �OrangeHRM� (expected)
# Close browser

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # from webdriver module we call Chrome class we created an object
# # driver = webdriver.Firefox()
# # driver = webdriver.Edge()
# driver.get("https://opensource-demo.orangehrmlive.com")
# driver.implicitly_wait(5)
# driver.find_element(By.XPATH,
#                     '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys(
#     'Admin')
# driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys('admin123')
# driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
# driver.implicitly_wait(5)
#
# act_title = driver.title
# exp_title = "OrangeHRM"
#
# if act_title == exp_title:
#     print('Login test passed')
# else:
#     print('login failed')
#
# driver.close()



# Open web browser
# Open url https://admin-demo.nopcommerce.com/login
# Provide email (admin@yourstore.com
# Provide password (admin)
# Click login
# Capture title
# Verify title Dashboard/ nopCommerce administration
# Close browser

driver.get("https://admin-demo.nopcommerce.com/login")
driver.find_element(By.ID, 'Email').clear()
driver.find_element(By.ID, "Email").send_keys('admin@yourstore.com')
driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Password").send_keys("admin")
driver.find_element(By.XPATH,
                    "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()
act_title = driver.title
exp_title = "Dashboard / nopCommerce administration"

if act_title == exp_title:
    print('Login test passed')
else:
    print('login failed')
driver.close()

