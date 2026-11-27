from pages.base_page import BasePage


class TextInputPage(BasePage):
    path = "/textinput"

    def __init__(self, page):
        super().__init__(page)
        self.input_field = page.locator("#newButtonName")
        self.button = page.locator("#updatingButton")

    def enter_text(self, text):
        self.input_field.press_sequentially(text)

    def click_button(self):
        self.button.click()

    def change_button_name(self, text):
        self.enter_text(text)
        self.click_button()