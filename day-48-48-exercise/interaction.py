from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# URL = "https://en.wikipedia.org/wiki/Main_Page"
URL = "http://secure-retreat-92358.herokuapp.com/"

driver.get(url=URL)
f_name = driver.find_element(By.NAME, "fName")
f_name.send_keys("Aliyu")
l_name = driver.find_element(By.NAME, "lName")
l_name.send_keys("Ahmad")
email = driver.find_element(By.NAME, "email")
email.send_keys("asdsdfssd60@gmail.com")

button_element = driver.find_element(By.CLASS_NAME, "btn")
button_element.click()

# stats_element = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(stats_element.text)
time.sleep(5)
driver.quit()


