#С помощью assert можно проверять любую конструкцию, которая возвращает True/False
from selenium import webdriver
import pytest
import time

from selenium.common.exceptions import NoSuchElementException

#Если нужно проверить, что тест вызывает ожидаемое исключение, использовать специальную конструкцию with pytest.raises()
def test_exception1(): #зафейлится, так как найдет кнопку, которая не должна быть. Ошибка NoSuchElementException, которую ожидает контекстный менеджер pytest.raises, не возникнет
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")
        #можно проверить, что на странице сайта не должен отображаться какой-то элемент
        with pytest.raises(NoSuchElementException):
            browser.find_element_by_css_selector("button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
            
    finally: 
        time.sleep(3)
        browser.quit()

def test_exception2():
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element_by_css_selector("no_such_button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
            
    finally: 
        time.sleep(3)
        browser.quit()