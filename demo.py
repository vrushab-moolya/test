from  selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(executable_path='./drivers/chromedriver.exe')
driver.get('https://www.saucedemo.com/')

driver.find_element(By.NAME, 'user-name').send_keys('standard_user')

driver.find_element(By.NAME, 'password').send_keys('secret_sauce')
driver.find_element(By.ID, 'login-button').click()

driver.find_element(By.XPATH,'(//div[@class="inventory_item_name"])[1]').click()

time.sleep(2)
cart=driver.find_element(By.XPATH,'//button[@class="btn_primary btn_inventory"]')
cart.click()










