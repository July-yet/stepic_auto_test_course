from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")    
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = int(browser.find_element(By.ID, "input_value").text)
    y = calc(x)
    input2 = browser.find_element(By.ID, "answer")
    input2.send_keys(y)

    button = browser.find_element(By.TAG_NAME, "button")    
    button.click()
    

finally:
    time.sleep(15)
    browser.quit()    