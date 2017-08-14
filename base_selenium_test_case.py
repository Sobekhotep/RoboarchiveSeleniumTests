import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unittest import TestCase

class BaseSeleniumTestCase(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def wait_for_element(self, locator, timeout=10, by=By.CSS_SELECTOR):
        """Function to wait for the element to appear on the page. Default timeout is 10 Sec, locator is CSS selector."""
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, locator))
        )
        return element

    def wait_for_element_disappear(self, locator, timeout=10, by=By.CSS_SELECTOR):
        """Function to wait for the element to disappear on the page. Default timeout is 10 Sec, locator is CSS selector."""
        element = WebDriverWait(self.driver, timeout).until_not(
            EC.presence_of_element_located((by, locator))
        )
        return element

    def assert_element_exists(self, driver, locator, by=By.CSS_SELECTOR):
        """Function to wait for the element exists on the page. Default locator is CSS selector."""
        try:
            driver.find_element(by, locator)
        except NoSuchElementException as e:
            self.fail('Element with selector {} not found'.format(locator))

    def assert_element_not_exist(self, driver, locator, by=By.CSS_SELECTOR):
        """Function to wait for the element exists on the page. Default locator is CSS selector."""
        try:
            driver.find_element(by, locator)
            self.fail('Element with selector {} found, which was not expected'.format(locator))
        except NoSuchElementException as e:
            pass

if __name__ == "__main__":
    unittest.main()
