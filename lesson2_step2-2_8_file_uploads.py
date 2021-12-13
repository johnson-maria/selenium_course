from selenium import webdriver
import os 
import time

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("TestName")

    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("TestLastName")

    input3 = browser.find_element_by_name("email")
    input3.send_keys("TestEmail")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(current_dir)
    file_path = os.path.join(current_dir, 'files-for-code', 'file.txt')
    print(file_path)


    file_button = browser.find_element_by_id("file")
    file_button.send_keys(file_path)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()