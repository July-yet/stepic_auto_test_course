from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value").text
    y = calc(x_element)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    input2 = browser.find_element(By.ID, "robotCheckbox")
    input2.click()
    input3= browser.find_element(By.ID, "robotsRule")
    input3.click()
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()    