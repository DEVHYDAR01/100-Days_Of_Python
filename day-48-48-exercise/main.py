from selenium.webdriver.common.by import By
from selenium import webdriver

URL = "https://www.python.org/"
driver = webdriver.Chrome()

driver.get(url=URL)
date_elements = driver.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery .menu time")
event_elements = driver.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery .menu a")
all_events = [event.text for event in event_elements]
all_dates = [date.text for date in date_elements]
convert_to_dict = {idx: {"time": value, "name": all_events[idx]} for idx, value in enumerate(all_dates)}
print(convert_to_dict)


driver.quit()
