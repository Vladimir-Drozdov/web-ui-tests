from pages.base_page import BasePage


class DynamicIdPage(BasePage):
    path = "/dynamicid"

    def __init__(self, page):
        super().__init__(page)
        self.button = page.locator("//button[text()='Button with Dynamic ID']")

    def click_button(self):
        self.button.click()

    def get_button_id(self):
        return self.button.get_attribute("id")