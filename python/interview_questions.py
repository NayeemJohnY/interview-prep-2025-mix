
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Interview questions
webdriver.Remote()
driver.get('https://google.com')

# Main

# Frame 1 -
driver.switch_to.frame('fram1')


driver.switch_to.default_content()

# Frame 2
driver.switch_to.frame(driver.find_element(By.XPATH, '//frame'))


# Multiple tabs
handles = driver.window_handles
abc = handles[3]

# Window / Tab = 4
driver.switch_to.window(abc)

# Webdriver
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if driver.title == "Webdriver":
        break


# other action
