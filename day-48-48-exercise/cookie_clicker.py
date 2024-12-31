from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome()

driver.get(url=URL)

cookie_element = driver.find_element(By.ID, "cookie")

while True:
    # Specify the duration in seconds
    duration = 10  # Task will run for 5 seconds
    start_time = time.time()

    # Perform the task within the given duration
    counter = 0
    while time.time() - start_time < duration:
        cookie_element.click()
        counter += 1

    print(f"Task completed with counter: {counter}")
    print("Task stopped after the timer.")

    elements = driver.find_elements(By.CSS_SELECTOR, "#store>div")
    elements_grayed = driver.find_elements(By.CSS_SELECTOR, '#store>div.grayed')
    money = int(driver.find_element(By.ID, "money").text.replace(",", ""))
    elements_values = [int(elements[i].text.strip().split("\n")[0].split("-")[1].replace(",", "")) for i in
                       range(len(elements) - 1)]
    # print(elements_values)

    not_grayed = [int(element.text.strip().split("\n")[0].split("-")[1].replace(",", "")) for element in elements if
                  element not in elements_grayed]
    # print(not_grayed)
    most_expensive = max(not_grayed)
    if money > most_expensive:
        get_index = elements_values.index(most_expensive)
        elements[get_index].click()




