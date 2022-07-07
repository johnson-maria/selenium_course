import pytest
import time
from pages.product_page import ProductPage
from pages.basket_page import BasketPage

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open() #Гость открывает страницу товара
    page.go_to_basket() #Переходит в корзину по кнопке в шапке 
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_book() #Ожидаем, что в корзине нет товаров
    basket_page.should_be_empty_basket() #Ожидаем, что есть текст о том что корзина пуста 


# запуск с параметром pytest -s -v --tb=line --language=en test_product_page.py