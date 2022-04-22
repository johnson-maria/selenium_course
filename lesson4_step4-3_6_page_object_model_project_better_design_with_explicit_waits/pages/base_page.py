import math
from selenium.common.exceptions import NoAlertPresentException #импорт нужного исключения
from selenium.common.exceptions import NoSuchElementException #импорт нужного исключения
from selenium.common.exceptions import TimeoutException #импорт нужного исключения
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    # добавим конструктор — метод, который вызывается, когда мы создаем объект. Конструктор объявляется ключевым словом __init__
    # browser прилетает из conftest.py, а url из файлов с тестами
    def __init__(self, browser, url, timeout=10): #добавим команду для неявного ожидания со значением по умолчанию в 10
        self.browser = browser
        self.url = url
        #self.browser.implicitly_wait(timeout)
    
    def open(self): # метод open. Он должен открывать нужную страницу в браузере, используя метод get()
        self.browser.get(self.url)

    def is_element_present(self, how, what): #перехват исключения. Два аргумента: как искать (css, id, xpath и тд) и что искать (строку-селектор) 
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4): #упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False   

    def is_disappeared(self, how, what, timeout=4): #будет ждать до тех пор, пока элемент не исчезнет
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what))) #WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
        except TimeoutException:
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