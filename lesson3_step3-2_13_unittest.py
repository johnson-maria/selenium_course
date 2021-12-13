from selenium import webdriver
import time
import unittest #Импортировать unittest в файл: import unittest

class TestAbs(unittest.TestCase): #Создать класс, который должен наследоваться от класса TestCase: class TestAbs(unittest.TestCase):
    def test_registration1(self): #Превратить тестовые функции в методы, добавив ссылку на экземпляр класса self в качестве первого аргумента функции: def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("div.first_block .first_class input")
        input1.send_keys("test_text")
        
        input2 = browser.find_element_by_css_selector("div.first_block .second_class input")
        input2.send_keys("test_text")
        
        input3 = browser.find_element_by_css_selector("div.first_block .third_class input")
        input3.send_keys("test_text") 

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be equal texts") #Изменить assert на self.assertEqual()
        
    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("div.first_block .first_class input")
        input1.send_keys("test_text")
        
        input2 = browser.find_element_by_css_selector("div.first_block .second_class input")
        input2.send_keys("test_text")
        
        input3 = browser.find_element_by_css_selector("div.first_block .third_class input")
        input3.send_keys("test_text") 

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be equal texts") #Изменить assert на self.assertEqual()
        
if __name__ == "__main__":
    unittest.main() #Заменить строку запуска программы на unittest.main()






