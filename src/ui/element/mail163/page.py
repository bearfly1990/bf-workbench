from src.ui.element.base import ElementBase


class Mail163PageMain(ElementBase):
    URL = "https://mail.163.com/"

    def __init__(self, driver):
        super().__init__(driver, "")
        self.login_page = LoginPage(driver)

    def visit_url(self):
        self.url(self.URL)


class LoginPage(ElementBase):
    xpath_username = "//input[@name='email']"
    xpath_password = "//input[@name='password']"
    xpath_submit = "//input[@id='dologin']"

    def __init__(self, driver):
        self.username = ElementBase(driver, self.xpath_username)
        self.password = ElementBase(driver, self.xpath_password)
        self.submit = ElementBase(driver, self.xpath_submit)
