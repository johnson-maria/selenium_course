from .base_page import BasePage #импорт базового класса BasePage
from selenium.webdriver.common.by import By
from locators import MainPageLocators
class MainPage(BasePage): #MainPage наследник класса BasePage. Класс-предок в Python указывается в скобках
    def go_to_login_page(self): #аргумент self для доступа к атрибутам и методам класса
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK) # символ * указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать
        login_link.click()
        # alert = self.browser.switch_to.alert
        # alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

        