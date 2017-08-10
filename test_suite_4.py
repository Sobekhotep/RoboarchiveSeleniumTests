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
        url = self.driver.current_url

        self.assertEqual(url, search_url)


if __name__ == "__main__":
    unittest.main()
