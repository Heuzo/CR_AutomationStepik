from selenium.webdriver.common.by import By
import time

def test_languages_basket_btn(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207')
    time.sleep(2)
    btn_basket = browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    assert btn_basket
