import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import TestCase



class MyFirstTest(TestCase):
    def test_ufa(self):
        driver = webdriver.Firefox()
        driver.get("http://roboarchive.org/search")
        self.assertIn("Robo Archive", driver.title)
        elem = driver.find_element_by_id("search-input")
        elem.send_keys("Уфа")
        elem.send_keys(Keys.RETURN)

    def test2(self):
        asdf

    def test3(self):
        x = 5
        self.assertEqual(x, 4)


if __name__ == "__main__":
    unittest.main()
