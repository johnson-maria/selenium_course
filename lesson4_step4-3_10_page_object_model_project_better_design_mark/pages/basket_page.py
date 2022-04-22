from .base_page import BasePage #импорт базового класса BasePage
from locators import BasketPageLocators


class BasketPage(BasePage):
    #Реализуйте там необходимые проверки, в том числе отрицательную, которую мы обсуждали в предыдущих шагах. 

    def should_not_be_book(self):
        assert self.is_not_element_present(*BasketPageLocators.BOOK_NAME), \
        "The book is presented, but should not be"

    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Basket is not empty"