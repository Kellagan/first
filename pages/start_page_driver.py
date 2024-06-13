import time

from pages.base_page import BasePage


def test(driver):
    page = BasePage(driver, 'https://jokerstars-test.vercel.app')
    page.open()
    time.sleep(10)