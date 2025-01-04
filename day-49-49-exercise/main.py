from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time

load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

driver = webdriver.Chrome()

driver.get(url=URL)
signin_btn = driver.find_element(By.XPATH, '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
signin_btn.send_keys(Keys.ENTER)

email_field = driver.find_element(By.ID, "base-sign-in-modal_session_key")
password_field = driver.find_element(By.ID, "base-sign-in-modal_session_password")
email_field.send_keys(username)
password_field.send_keys(password)

welcome_back_signin = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
welcome_back_signin.send_keys(Keys.ENTER)

# You may be presented with a CAPTCHA - Solve the Puzzle Manually
input("Press Enter when you have solved the Captcha")

# jobs_elements = driver.find_elements(By.CSS_SELECTOR, ".ember-view.display-flex")
# print(jobs_elements)

job_elements = driver.find_elements(By.CLASS_NAME, "job-card-container--clickable")
print(job_elements)
job_elements[1].click()
for job in job_elements:
    save_job = driver.find_element(By.CLASS_NAME, 'jobs-save-button')
    save_job.send_keys(Keys.ENTER)
    company_post = driver.find_element(By.CLASS_NAME,
                                   "PvaypIWSSzaYekZGVDZTENtvQwtUaxUmatY")
    company_post.send_keys(Keys.ENTER)
    follow_company = driver.find_element(By.CLASS_NAME,'follow-button__follow')
    driver.back()
    time.sleep(5)
    job.click()