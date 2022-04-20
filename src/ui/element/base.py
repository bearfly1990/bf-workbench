import logging
import time

from selenium.common.exceptions import TimeoutException, NoAlertPresentException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

logger = logging.getLogger()


class WebTestBase:
    def __init__(self, driver : WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def wait_for_present(self, element) -> WebElement:
        return self.wait.until(expected_conditions.presence_of_element_located(element))

    def wait_for_clickable(self, element):
        return self.wait.until(expected_conditions.element_to_be_clickable(element))

    def wait_for_alert(self):
        self.wait.util(expected_conditions.alert_is_present(), 'Timeout waiting for Alert')

    def input(self, element, val):
        self.wait_for_present(element).send_keys(val)

    def click(self, element):
        time.sleep(1)
        self.wait_for_clickable(element).click()

    def get_text(self, element):
        return self.wait_for_present(element).text

    def url(self, addr):
        self.driver.get(addr)

    def get(self, element):
        self.wait_for_present(element).find_element(*element)

    def display(self, element):
        self.wait_for_present(element).find_element(*element).is_displayed();

    def accept_alert(self):
        try:
            self.wait_for_alert()
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            alert.accept()
            return alert_text
        except TimeoutException:
            logger.warning('No Alert Found')

    def is_element_present(self, element):
        elements = self.driver.find_elements(*element)
        return True if elements else False

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True


class ElementBase(WebTestBase):
    def __init__(self, driver, element):
        super(ElementBase, self).__init__(driver)
        if isinstance(element, str):
            self.element = (By.XPATH, element)
        else:
            self.element = element

    def click(self):
        super().click(self.element)

    def get_text(self):
        return super().get_text(self.element)

    def input(self, val):
        super().input(self.element, val)

    def itself(self):
        super().get(self.element)

    def exists(self):
        return super().is_element_present(self.element)

    def display(self):
        return super().display(self.element)



