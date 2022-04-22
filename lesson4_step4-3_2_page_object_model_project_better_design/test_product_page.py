import time
from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    time.sleep(5)
    product_page.should_be_add_button()
    time.sleep(5)
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    time.sleep(5)
    product_page.should_see_message_about_successful_adding_product_to_basket()
    product_page.should_see_message_of_basket_total()
    product_page.should_see_book_name()
    product_page.should_see_book_price()
    product_page.should_be_equal_book_name()
    product_page.should_be_equal_book_price()


# запуск с параметром pytest -s -v --tb=line --language=en test_product_page.py