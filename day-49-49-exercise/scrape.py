from selenium import webdriver

driver = webdriver.Chrome()
URL = "https://portal.nysc.org.ng/nysc4/ResumePayment.aspx"

while True:
    driver.get(url=URL)
