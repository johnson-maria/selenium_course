from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():

    @classmethod # setup_class(self) и teardown_class(self) вместе с @classmethod запускаются один раз перед всеми методами (setup) и закрываются также один раз (teardown)
    def setup_class(self):
        print("\nstart browser for test suite 1 ..")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite 1 ..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print('start test link 1')
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print('start test basket 1')
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")


class TestMainPage2(): 

    def setup_method(self): #Когда определен метод setUp(), бегун теста будет выполнять этот метод перед каждым испытанием
        print("start browser for test 2..") #setup_method(self) и teardown_method(self) оборачивается каждый исполняемый метод
        self.browser = webdriver.Chrome()

    def teardown_method(self): #если определен метод tearDown(), то Test runner будет вызывать этот метод после каждого теста
        print("quit browser for test 2..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print('start test link 2')
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print('start test basket 2')
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")