link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

    # (selenium_env) D:\Projects\selenium_course\lesson3_step3-6_6_geckodriver_and_chromedriver>pytest -s -v --browser_name=firefox lesson3_step3-6_6_browser-name_test.py
    # или: pytest -s -v --browser_name=chrome lesson3_step3-6_6_browser-name_test.py