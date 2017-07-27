import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from unittest import TestCase


def wait_for_element_by_css(driver, css_selector, timeout=10):
    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
    )
    return element


class BaseSeleniumTestCase(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def assert_css_selector_exists(self, driver, css_selector):
        try:
            driver.find_element_by_css_selector(css_selector)
        except NoSuchElementException as e:
            self.fail('Element with selector {} not found'.format(css_selector))


class TestSearchField(BaseSeleniumTestCase):
    def test_empty_search_field(self):

        self.driver.get("http://roboarchive.org/search")

        search_input = wait_for_element_by_css(self.driver, "#search-input")

        button = wait_for_element_by_css(self.driver, "#search-button")
        button.click()

        results_element = wait_for_element_by_css(self.driver, "#search-results")
        self.assert_css_selector_exists(self.driver, '.search-result-item')

    def test_search_field_with_russian_a(self):
        self.driver.get("http://roboarchive.org/search")

        search_input = wait_for_element_by_css(self.driver, "#search-input")

        elem = self.driver.find_element_by_id("search-input")
        elem.send_keys("а")

        button = wait_for_element_by_css(self.driver, "#search-button")
        button.click()

        results_element = wait_for_element_by_css(self.driver, "#search-results")
        self.assert_css_selector_exists(self.driver, '.search-result-item')

    def test_search_field_with_russian_A(self):
        self.driver.get("http://roboarchive.org/search")

        search_input = wait_for_element_by_css(self.driver, "#search-input")

        elem = self.driver.find_element_by_id("search-input")
        elem.send_keys("А")

        button = wait_for_element_by_css(self.driver, "#search-button")
        button.click()

        results_element = wait_for_element_by_css(self.driver, "#search-results")
        self.assert_css_selector_exists(self.driver, '.search-result-item')

    def test_search_field_with_space(self):
        self.driver.get("http://roboarchive.org/search")

        search_input = wait_for_element_by_css(self.driver, "#search-input")

        elem = self.driver.find_element_by_id("search-input")
        elem.send_keys(" ")

        button = wait_for_element_by_css(self.driver, "#search-button")
        button.click()

        results_element = wait_for_element_by_css(self.driver, "#search-results")
        self.assert_css_selector_exists(self.driver, '.search-result-item')


if __name__ == "__main__":
    unittest.main()




