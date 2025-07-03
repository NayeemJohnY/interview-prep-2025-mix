# Write a Program to char and seq
# input = aaaabbbccdeeefggg
# output = "a4b3c2d1e3f1g3"
# Solution 1
input = "aaaabbbccdeeefggg"
last_char = input[0]
counter = 1
output = ""
for i in range(1, len(input)):
    if input[i] == last_char:
        counter += 1
    else:
        output += last_char + str(counter)
        counter = 1
        last_char = input[i]
output += last_char + str(counter)
print(output)

# Solution 2
counter = 1
output = ""
for i in range(1, len(input)):
    if input[i] == input[i-1]:
        counter += 1
    else:
        output += input[i-1] + str(counter)
        counter = 1
        last_char = input[i]
output += input[i-1] + str(counter)
print(output)

# Write a Program to print the repetition indices of charachters in a String.
#  inp - "i love to code" ... e.g for e the output will be - [5,13]
#i=[0]
#l=[1]
#O=[3,6,8]

inp = "i love to code"
inp = inp.replace(" ", "")
freq_map = {}
for i, ch in enumerate(inp):
    if ch in freq_map:
        freq_map[ch].append(i)
    else:
        freq_map[ch] = [i]
print(freq_map)


# Write Xpath to select Price from Day15 - day 25
x = ('//*[@class="DayPicker-Month"][descendant::*[text()="August 2025"]]'
     '/descendant::*[@class="DayPicker-Day" ][descendant::p[text()>=15] and descendant::p[text() <=25]]'
     '/descendant::*[contains(@class,"todayPrice")]')
for i in x:
    print(i.textContent)

# Dynamic Pop up 
import functools
from selenium.webdriver.common.by import By
popup_close_button = (By.XPATH, '//*[contains(@class, "close")]')
def handle_popup(func):
    @functools.wraps(func)
    def wrapper(driver_ops, *args, **kwargs):
        if driver_ops.is_element_present(
                popup_close_button, "Pop up close Icon", wait_time=1):
            driver_ops.click(
                popup_close_button, "Pop up close Icon")
        return func(driver_ops, *args, **kwargs)
    return wrapper

@handle_popup
def click(driver_ops, locator, elem_name):
    driver_ops.click(
        locator, elem_name)

# Get all ids => features -> properties -> @id
import requests
import json

response = requests.get(url="https://api.weather.gov/stations")
res = json.loads(response.text)
ids = [feature["properties"]["@id"] for feature in res['features']]
print(ids)