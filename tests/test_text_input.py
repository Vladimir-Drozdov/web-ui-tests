import allure
import pytest
from playwright.sync_api import expect

from pages.text_input_page import TextInputPage

NAMES = ["Hello", "QA", "New button name 123"]


@allure.feature("Text Input")
@allure.title("Кнопка меняет название на {name}")
@pytest.mark.parametrize("name", NAMES)
def test_change_button_name(page, name):
    text_page = TextInputPage(page)
    text_page.open()
    text_page.change_button_name(name)
    expect(text_page.button).to_have_text(name)


@allure.feature("Text Input")
@allure.title("Без ввода текста название кнопки не меняется")
def test_button_name_without_input(page):
    text_page = TextInputPage(page)
    text_page.open()
    old_name = text_page.button.inner_text()
    text_page.click_button()
    expect(text_page.button).to_have_text(old_name)