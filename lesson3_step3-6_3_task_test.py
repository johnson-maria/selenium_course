import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', 
["https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"])
class TestLogin:
    def test_should_be_correct(self, browser, link):
        browser.get(f"{link}")      
        input = browser.find_element_by_css_selector("textarea")
        answer = str(math.log(int(time.time())))
        input.send_keys(answer)
        button = browser.find_element_by_css_selector("button.submit-submission")
        button.click()
        text_in_element = browser.find_element_by_css_selector("pre.smart-hints__hint")
        print(text_in_element.text + " : Answer")
        assert text_in_element.text == "Correct!", "Text element should be equal 'Correct!'"
        