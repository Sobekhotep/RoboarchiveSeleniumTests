from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import TestCase



class MyFirstTest(TestCase):
    def test_ufa(self):
        driver = webdriver.Firefox()
        driver.get("http://roboarchive.org/search")
        assert "Robo Archive" in driver.title
        elem = driver.find_element_by_id("search-input")
        elem.send_keys("Уфа")
        elem.send_keys(Keys.RETURN)

    def test2(self):
        pass

    def test3(self):
        pass
    
