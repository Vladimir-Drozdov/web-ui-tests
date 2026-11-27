from pages.base_page import BasePage


class VerifyTextPage(BasePage):
    path = "/verifytext"

    def __init__(self, page):
        super().__init__(page)
        self.welcome_css = page.locator(".bg-primary .badge-secondary")
        self.welcome_xpath = page.locator("//span[normalize-space(.)='Welcome UserName!']")