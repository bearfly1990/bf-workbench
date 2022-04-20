import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from src.ui.element.baidu.page import BaiduPageMain
from src.util.api import BFWBAPIClient
from setting import *


@pytest.fixture(scope='session', autouse=True)
def driver(request):
    chrome_driver_path = 'resources/driver/chromedriver.exe'
    chrome_options = Options()
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='session', autouse=True)
def baidu_main_page(request, driver):
    baidu_main_page = BaiduPageMain(driver)
    driver.get(BaiduPageMain.URL)
    yield baidu_main_page


@pytest.fixture(scope='session', autouse=True)
def api_client(request, driver):
    api_client = BFWBAPIClient(API_SITE_URL, headers=HEADERS_DEFAULT, proxies=PROXY_DICT_DEFAULT)
    yield api_client
