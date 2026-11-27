from config.settings import BASE_URL


class BasePage:
    path = ""

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(BASE_URL + self.path)
        return self

    def reload(self):
        self.page.reload()