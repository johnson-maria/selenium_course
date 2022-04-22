import math
from selenium.common.exceptions import NoAlertPresentException #импорт нужного исключения
from selenium.common.exceptions import NoSuchElementException #импорт нужного исключения

class BasePage():
    # добавим конструктор — метод, который вызывается, когда мы создаем объект. Конструктор объявляется ключевым словом __init__
    # browser прилетает из conftest.py, а url из файлов с тестами
    def __init__(self, browser, url, timeout=10): #добавим команду для неявного ожидания со значением по умолчанию в 10
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    
    def open(self): # метод open. Он должен открывать нужную страницу в браузере, используя метод get()
        self.browser.get(self.url)

    def is_element_present(self, how, what): #перехват исключения. Два аргумента: как искать (css, id, xpath и тд) и что искать (строку-селектор) 
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def solve_quiz_and_get_code(self): #метод для получения проверочного кода
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")