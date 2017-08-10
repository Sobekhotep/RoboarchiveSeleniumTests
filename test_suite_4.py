from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unittest import TestCase

class BaseSeleniumTestCase(TestCase):

    driver = webdriver.Firefox()
    driver.get("http://roboarchive.org/search")

    def wait_for_element(driver, locator, timeout=10, by=By.CSS_SELECTOR):
      element = WebDriverWait(driver, timeout).until(
          EC.presence_of_element_located((by, locator))
      )
      return element

class TestURLField(BaseSeleniumTestCase):

    def test_url_after_click_search(self):
        assert "roboarchive.org" in driver.current_url

if __name__ == "__main__":
    unittest.main()
