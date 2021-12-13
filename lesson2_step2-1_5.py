from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    

    
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    
    
 
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()


    button = browser.find_element_by_css_selector("button.btn")
    button.click()


    time.sleep(1)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    