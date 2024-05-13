from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Firefox()
driver.get('https://rg.ru/?auth=modal')

mail=driver.find_element(By.ID,'email')
psw=driver.find_element(By.ID,'password')
btn=driver.find_element(By.CLASS_NAME,'AuthFormTemplate_button__Bl_Pw ')
mail.clear()
mail.send_keys('druzhkovayana9@gmail.com')
psw.clear()
psw.send_keys('@Rpfbed36H#yM;5')
btn.click()
print(driver.title)
time.sleep(1)
driver.close()