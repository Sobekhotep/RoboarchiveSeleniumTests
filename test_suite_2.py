import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from unittest import TestCase

def wait_for_element(driver, locator, timeout=10, by=By.CSS_SELECTOR):
    """Function to wait for the element to appear on the page. Default timeout is 10 Sec, locator is CSS selector."""
    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, locator))
    )
    return element

def wait_for_element_disappear(driver, locator, timeout=10, by=By.CSS_SELECTOR):
    """Function to wait for the element to disappear on the page. Default timeout is 10 Sec, locator is CSS selector."""
    element = WebDriverWait(driver, timeout).until_not(
        EC.presence_of_element_located((by, locator))
    )
    return element

class BaseSeleniumTestCase(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

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


class TestSearchField(BaseSeleniumTestCase):

    def prepare_search_test(self):
        self.driver.get("http://roboarchive.org/search")
        search_input = wait_for_element(self.driver, "#search-input")
        elem = self.driver.find_element_by_id("search-input")
        return elem

    def test_empty_search_field(self):

        self.driver.get("http://roboarchive.org/search")

        search_input = wait_for_element(self.driver, "#search-input")

        button = wait_for_element(self.driver, "#search-button")
        button.click()

        results_element = wait_for_element(self.driver, "#search-results")
        self.assert_element_exists(self.driver, '.search-result-item')

    def test_search_field_with_russian_a(self):
        elem = self.prepare_search_test()
        elem.send_keys("а")

        button = wait_for_element(self.driver, "#search-button")
        button.click()

        results_element = wait_for_element(self.driver, "#search-results")
        self.assert_element_exists(self.driver, '.search-result-item')

    def test_search_field_with_russian_A(self):
        elem = self.prepare_search_test()
        elem.send_keys("А")

        button = wait_for_element(self.driver, "#search-button")
        button.click()

        results_element = wait_for_element(self.driver, "#search-results")
        self.assert_element_exists(self.driver, '.search-result-item')

    def test_search_field_with_space(self):
        elem = self.prepare_search_test()
        elem.send_keys(" ")

        button = wait_for_element(self.driver, "#search-button")
        button.click()

        results_element = wait_for_element(self.driver, "#search-results")
        self.assert_element_exists(self.driver, '.search-result-item')

    def test_search_field_with_point(self):
        elem = self.prepare_search_test()
        elem.send_keys(".")

        button = wait_for_element(self.driver, "#search-button")
        button.click()

        results_element = wait_for_element(self.driver, "#search-results")
        self.assert_element_exists(self.driver, '.search-result-item')

    def test_search_field_with_at(self):
        elem = self.prepare_search_test()
        elem.send_keys("@")

        button = wait_for_element(self.driver, "#search-button")
        button.click()

        results_element = wait_for_element(self.driver, "//div[. = 'Поиск...']", by=By.XPATH)
        results_element_disappear = wait_for_element_disappear(self.driver, "//div[. = 'Поиск...']", by=By.XPATH)
        self.assert_element_not_exist(self.driver, "#search-results")

    def test_search_field_with_ufa(self):
        elem = self.prepare_search_test()
        elem.send_keys("Уфа")

        button = wait_for_element(self.driver, "#search-button")
        button.click()

        results_element = wait_for_element(self.driver, "#search-results")
        self.assert_element_exists(self.driver, '.search-result-item')

    def test_search_field_with_guberniya(self):
        elem = self.prepare_search_test()
        elem.send_keys("губерния")

        button = wait_for_element(self.driver, "#search-button")
        button.click()

        results_element = wait_for_element(self.driver, "#search-results", timeout=30)
        self.assert_element_exists(self.driver, '.search-result-item')

if __name__ == "__main__":
    unittest.main()




