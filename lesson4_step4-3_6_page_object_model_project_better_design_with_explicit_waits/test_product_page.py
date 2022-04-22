import pytest
import time
from pages.product_page import ProductPage


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207//?promo=offer1"
    product_page = ProductPage(browser, link) 
    product_page.open() #Открываем страницу товара
    product_page.add_product_to_basket() #Добавляем товар в корзину 
    product_page.should_not_be_success_message() #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
 

def test_guest_cant_see_success_message(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207//?promo=offer1"
    product_page = ProductPage(browser, link)
    product_page.open() #Открываем страницу товара
    product_page.should_not_be_success_message() #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
 

def test_message_disappeared_after_adding_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207//?promo=offer1"
    product_page = ProductPage(browser, link)
    product_page.open() #Открываем страницу товара
    product_page.add_product_to_basket() #Добавляем товар в корзину 
    product_page.should_disappear() #Проверяем, что нет сообщения об успехе с помощью is_disappeared


# запуск с параметром pytest -s -v --tb=line --language=en test_product_page.py