import allure
import pytest

from setting import TEST_MODE, DEV
from src.test.base import TestBase
from src.ui.element.baidu.page import BaiduPageMain


@allure.feature("Test Basic Github Login")
@pytest.mark.incremental
@pytest.mark.skipif(TEST_MODE == DEV, reason="Skip On Test Case Development Mode")
@allure.story('Login')
class LoginTest(TestBase):

    @allure.story('Skip')
    @pytest.mark.skip()
    def test_skip_case(self, api_client):
        api_client.post('/test', json={"test": "test"})

    @allure.story('UserName')
    @allure.step("input username")
    def test_input_username(self, baidu_main_page: BaiduPageMain):
        print("XXXX2", baidu_main_page.driver)
        baidu_main_page.login_page.search.input("test")

    @allure.step("input password")
    # @pytest.mark.skip()
    def test_input_password(self, baidu_main_page: BaiduPageMain):
        pass

    @allure.story('Submit')
    @allure.step("input submit")
    @pytest.mark.cx
    def test_submit(self, baidu_main_page: BaiduPageMain):
        pass
