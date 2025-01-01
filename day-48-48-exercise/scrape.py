from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

path = "~/.config/google-chrome/Default/Extensions/ophjlpahpchlmihnnnihgmmeilfjmjjc/3.6.1_0"
chrome_options = Options()
chrome_options.add_argument(f"--load-extension={path}")

driver = webdriver.Chrome(options=chrome_options)

# Open any URL (e.g., chrome://newtab/)
driver.get("chrome-extension://ophjlpahpchlmihnnnihgmmeilfjmjjc/index.html")

# Click on the extension icon
# Note: This might require finding the extension UI in DevTools
action = ActionChains(driver)
# extension_button = driver.find_element("css selector", "selector-for-extension-icon")
# action.move_to_element(extension_button).click().perform()
#
# # Interact with the popup (if any)
# driver.switch_to.window(driver.window_handles[-1])  # Switch to popup window
# popup_element = driver.find_element("css selector", "selector-for-popup-element")
# popup_element.click()

time.sleep(70)
driver.quit()