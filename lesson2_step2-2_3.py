from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    number1 = int(browser.find_element_by_id("num1").text)
    number2 = int(browser.find_element_by_id("num2").text)
    
    # Проверка типа аргумента print(type(number1))
    
    sum = str(number1 + number2)

    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum) 
    
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    