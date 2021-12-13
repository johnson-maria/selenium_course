link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#magic_link")

    # (selenium_env) D:\Projects\selenium_course\lesson3_step3-6_6_geckodriver>pytest -v --tb=line --reruns 1 --browser_name=chrome lesson3_step3-6_7_rerun_test.py