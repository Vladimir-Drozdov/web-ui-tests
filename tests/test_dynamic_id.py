import allure
from playwright.sync_api import expect

from pages.dynamic_id_page import DynamicIdPage


@allure.feature("Dynamic ID")
@allure.title("Кнопку можно найти без id, id каждый раз новый")
def test_dynamic_id(page):
    dynamic_page = DynamicIdPage(page)
    dynamic_page.open()
    id_before = dynamic_page.get_button_id()
    dynamic_page.reload()
    id_after = dynamic_page.get_button_id()

    assert id_before != id_after
    dynamic_page.click_button()
    expect(dynamic_page.button).to_be_enabled()