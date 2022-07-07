from .base_page import BasePage
from locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self): #метод для добавления в корзину
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON) # символ * указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать
        add_button.click()

    def should_be_equal_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        assert book_name.text == success_message.text, f"Name of a product in basket should be equal book name {book_name.text} and {success_message}"

    def should_be_equal_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        assert book_price.text == basket_total.text, f"Price in basket total should be equal book price {book_price.text} and {basket_total.text}"

    def should_be_add_button(self):    #Дописать методы-проверки
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Add button is not presented"

    def should_see_message_about_successful_adding_product_to_basket(self):    #Дописать методы-проверки
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Successful message is not presented"
        #Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.

    def should_see_message_of_basket_total(self):    #Дописать методы-проверки
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL), "Message about total basket is not presented"
        #Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара. 
        
    def should_see_book_name(self):    
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME), "Book name is not presented"

        
    def should_see_book_price(self): 
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE), "Book price is not presented"
