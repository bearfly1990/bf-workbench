from src.ui.element.base import ElementBase


class GithubPageMain(ElementBase):
    URL = "https://github.com/login"

    def __init__(self, driver):
        super().__init__(driver, "")
        self.login_page = LoginPage(driver)

    def visit_url(self):
        self.url(self.URL)


class LoginPage(ElementBase):
    __xpath_username = "//input[@name='login']"
    __xpath_password = "//input[@name='password']"
    __xpath_submit = "//input[@name='submit']"

    def __init__(self, driver):
        self.username = ElementBase(driver, self.__xpath_username)
        self.password = ElementBase(driver, self.__xpath_password)
        self.submit = ElementBase(driver, self.__xpath_submit)
