from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from time import sleep


class Region:
    """
        class to handle region(parent class for pages)
    """
    META_LANGUAGE = (By.XPATH, "//meta[@http-equiv='Content-Language']")

    def __init__(self, driver: webdriver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 15)

    def wait(self, locator: tuple):
        """
            wait handler for more beauty
        :return:
        """
        return self._wait.until(ec.presence_of_element_located(locator))

    def is_visible(self, locator: tuple):
        """
            wait handler for visibility
        :param locator:
        :return:
        """
        return  self._wait.until(ec.visibility_of_element_located(locator))

    def not_visible(self, locator: tuple):
        """
            wait for not visibility
        :param locator:
        :return:
        """
        return self._wait.until_not(ec.visibility_of_element_located(locator))

    def find(self, locator: tuple):
        """
            webelement handler
        :param locator:
        :return:
        """
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        """
            list of webelements handler
        :param locator:
        :return:
        """
        return self.driver.find_elements(*locator)

    def wait_for_alert(self):
        return self._wait.until(ec.alert_is_present())

    @staticmethod
    def dummy_wait(time: float = 1):
        sleep(time)

    def get_current_localization(self) -> str:
        return self.wait(self.META_LANGUAGE).get_attribute("content")
