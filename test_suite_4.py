import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unittest import TestCase

from test_suite_2 import BaseSeleniumTestCase


class TestURLField(BaseSeleniumTestCase):

    def test_url_after_click_search(self):
        search_url = "http://roboarchive.org/search"
        self.driver.get(search_url)

        button = self.wait_for_element("#search-button")
        button.click()

        self.wait_for_element('.search-result-item')

        url = "http://roboarchive.org/search?docdescription=false&doctitle=false&emptysearch=true&" \
              "fromdate=&gasrb=false&niab=false&page=1&search=&todate="

        self.assertEqual(self.driver.current_url, url)


if __name__ == "__main__":
    unittest.main()
