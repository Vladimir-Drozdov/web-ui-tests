import allure
from playwright.sync_api import expect

from pages.verify_text_page import VerifyTextPage


@allure.feature("Verify Text")
@allure.title("Текст Welcome UserName! находится по CSS")
def test_welcome_text_css(page):
    verify_page = VerifyTextPage(page)
    verify_page.open()
    expect(verify_page.welcome_css).to_be_visible()
    expect(verify_page.welcome_css).to_have_text("Welcome UserName!")


@allure.feature("Verify Text")
@allure.title("Текст Welcome UserName! находится по XPath")
def test_welcome_text_xpath(page):
    verify_page = VerifyTextPage(page)
    verify_page.open()
    expect(verify_page.welcome_xpath).to_have_count(1)
    expect(verify_page.welcome_xpath).to_be_visible()