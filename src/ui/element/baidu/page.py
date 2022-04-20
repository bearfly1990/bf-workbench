from src.ui.element.base import ElementBase


class BaiduPageMain(ElementBase):
    URL = "http://www.baidu.com"

    def __init__(self, driver):
        super().__init__(driver, "")
        self.login_page = LoginPage(driver)

    def visit_url(self):
        self.url(self.URL)


class LoginPage(ElementBase):
    __xpath_search = "//input[@id='kw']"

    def __init__(self, driver):
        self.search = ElementBase(driver, self.__xpath_search)
