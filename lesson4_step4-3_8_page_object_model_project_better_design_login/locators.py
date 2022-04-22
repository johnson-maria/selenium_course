#вынос селекторов во внешнюю переменную
from selenium.webdriver.common.by import By

#Каждый класс будет соответствовать каждому классу PageObject

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) > .alertinner > strong") #1 элемент alertinner
    BASKET_TOTAL = (By.CSS_SELECTOR, "#messages > .alert:nth-child(3) > .alertinner > p:nth-child(1) > strong") #3 элемент alertinner
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")