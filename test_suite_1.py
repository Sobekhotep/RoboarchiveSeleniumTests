import unittest
from selenium.webdriver.common.by import By
from base_selenium_test_case import BaseSeleniumTestCase

class TestSearchField(BaseSeleniumTestCase):

    def prepare_search_test(self):
        self.driver.get("http://roboarchive.org/search")
        search_input = self.wait_for_element("#search-input")
        elem         = self.driver.find_element_by_id("search-input")
        return elem

    def test_empty_search_field(self):
        elem = self.prepare_search_test()

        button = self.wait_for_element("#search-button")
        button.click()

        results_element = self.wait_for_element("#search-results")
        self.assert_element_exists(self.driver, ".search-result-item")

    def test_search_field_with_russian_a(self):
        elem = self.prepare_search_test()
        elem.send_keys("а")

        button = self.wait_for_element("#search-button")
        button.click()

        results_element = self.wait_for_element("#search-results")
        self.assert_element_exists(self.driver, '.search-result-item')

    def test_search_field_with_russian_A(self):
        elem = self.prepare_search_test()
        elem.send_keys("А")

        button = self.wait_for_element("#search-button")
        button.click()

        results_element = self.wait_for_element("#search-results")
        self.assert_element_exists(self.driver, '.search-result-item')

    def test_search_field_with_space(self):
        elem = self.prepare_search_test()
        elem.send_keys(" ")

        button = self.wait_for_element("#search-button")
        button.click()

        results_element = self.wait_for_element("#search-results")
        self.assert_element_exists(self.driver, '.search-result-item')

    def test_search_field_with_point(self):
        elem = self.prepare_search_test()
        elem.send_keys(".")

        button = self.wait_for_element("#search-button")
        button.click()

        results_element = self.wait_for_element("#search-results")
        self.assert_element_exists(self.driver, '.search-result-item')

    def test_search_field_with_english_1a(self):
        elem = self.prepare_search_test()
        elem.send_keys("1a")

        button = self.wait_for_element("#search-button")
        button.click()

        results_element_disappear = self.wait_for_element_disappear("//div[. = 'Поиск...']", by=By.XPATH)
        self.assert_element_not_exist(self.driver, "#search-results")

    def test_search_field_with_at(self):
        elem = self.prepare_search_test()
        elem.send_keys("@")

        button = self.wait_for_element("#search-button")
        button.click()

        results_element_disappear = self.wait_for_element_disappear("//div[. = 'Поиск...']", by=By.XPATH)
        self.assert_element_not_exist(self.driver, "#search-results")

    def test_search_field_with_ufa(self):
        elem = self.prepare_search_test()
        elem.send_keys("Уфа")

        button = self.wait_for_element("#search-button")
        button.click()

        results_element = self.wait_for_element("#search-results")
        self.assert_element_exists(self.driver, '.search-result-item')

    def test_search_field_with_guberniya(self):
        elem = self.prepare_search_test()
        elem.send_keys("губерния")

        button = self.wait_for_element("#search-button")
        button.click()

        results_element = self.wait_for_element("#search-results",)
        self.assert_element_exists(self.driver, '.search-result-item')

    def test_search_field_with_minsk(self):
        elem = self.prepare_search_test()
        elem.send_keys("Минск")

        button = self.wait_for_element("#search-button")
        button.click()

        results_element = self.wait_for_element("#search-results",)
        self.assert_element_exists(self.driver, '.search-result-item')

if __name__ == "__main__":
    unittest.main()




