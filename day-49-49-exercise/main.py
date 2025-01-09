import selenium.common
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    StaleElementReferenceException,
    NoSuchElementException,
    ElementClickInterceptedException,
)
from dotenv import load_dotenv
import os
import time

# Load environment variables
load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get(url=URL)

# Log in
try:
    signin_btn = driver.find_element(By.XPATH,
                                     '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
    signin_btn.send_keys(Keys.ENTER)
except selenium.common.NoSuchElementException:
    print("No such element, trying to continue...")

email_field = driver.find_element(By.ID, "base-sign-in-modal_session_key")
password_field = driver.find_element(By.ID, "base-sign-in-modal_session_password")
email_field.send_keys(username)
password_field.send_keys(password)

welcome_back_signin = driver.find_element(By.XPATH,
                                          '//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
welcome_back_signin.send_keys(Keys.ENTER)

# Solve CAPTCHA manually if required
input("Press Enter when you have solved the CAPTCHA")

# Scroll within the job list to load more postings
scrollable_div = driver.find_element(By.CLASS_NAME, "qwiaGHkwlrieAZoYusFyjMXGbewtMHNtc")
for i in range(5):
    driver.execute_script("arguments[0].scrollTop += 500", scrollable_div)
    time.sleep(1)


# Retry logic for safe clicking
def safe_click(element):
    retries = 5
    for attempt in range(retries):
        try:
            element.click()
            return
        except (StaleElementReferenceException, ElementClickInterceptedException) as e:
            print(f"Error clicking element: {e}. Retrying {attempt + 1}/{retries}...")
            time.sleep(1)
    print("Failed to click element after retries.")


# Locate job elements
ul_element = driver.find_element(By.CLASS_NAME, "FRRHBcSAMYNTqdBkJBCtURynxFrHdvwBLeA")
job_elements = ul_element.find_elements(By.CSS_SELECTOR, "[data-job-id]")
print("Number of job postings found:", len(job_elements))

# Process each job posting
for index, job in enumerate(job_elements):
    try:
        # Re-locate job elements due to DOM changes
        job_elements = ul_element.find_elements(By.CSS_SELECTOR, "[data-job-id]")
        job = job_elements[index]

        # Click the job card
        safe_click(job)

        # Save the job
        save_job = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'jobs-save-button'))
        )
        save_job.send_keys(Keys.ENTER)

        # Navigate to the company page
        company_post = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "PvaypIWSSzaYekZGVDZTENtvQwtUaxUmatY"))
        )
        company_post.send_keys(Keys.ENTER)
        time.sleep(5)  # Allow time for the company page to load

        # Follow the company
        try:
            follow_company = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'follow'))
            )
            follow_company.click()
            print(f"Followed company for job {index + 1}")
        except NoSuchElementException:
            print(f"Follow button not found for job {index + 1}")
        except Exception as e:
            print(f"Error following company for job {index + 1}: {e}")

        # Return to the previous page
        driver.back()
        time.sleep(3)  # Wait for the page to reload

        print(f"Job {index + 1} processed successfully.")

    except Exception as e:
        print(f"Error processing job {index + 1}: {e}")

# Final visual confirmation and cleanup
time.sleep(5)
driver.quit()

# company_post = driver.find_element(By.CLASS_NAME, "PvaypIWSSzaYekZGVDZTENtvQwtUaxUmatY")
# company_post.send_keys(Keys.ENTER)
# time.sleep(10)
# follow_company = driver.find_element(By.CLASS_NAME, 'follow')
# follow_company.click()
# driver.back()
# job_elements[job].click()


