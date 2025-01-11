from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://tinder.com/"


driver = webdriver.Chrome()
driver.get(url=URL)
print("Page loaded successfully!!")

cookie_accept = driver.find_element(By.XPATH, '//*[@id="s-1453859685"]/div/div[2]/div/div/div[1]/div[1]/button')
cookie_accept.click()

login_btn = driver.find_element(By.CLASS_NAME, "Mx(12px) Mx(8px)--m")
login_btn.click()

time.sleep(1000000000)