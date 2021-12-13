import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
# time.sleep(30) 

def test_guest_should_see_add_to_cart_button(browser):
    browser.get(link)
    cart = browser.find_elements_by_css_selector("#add_to_basket_form")
    assert cart, "На странице присутствует кнопка 'Добавить в корзину'"

# Запуск теста: pytest --language=es test_items.py
# Запуск для проверяющего: pytest --language=fr test_items.py