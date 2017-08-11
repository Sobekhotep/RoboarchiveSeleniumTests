import unittest

from base_selenium_test_case import BaseSeleniumTestCase

from urllib.parse import urlparse
from urllib.parse import parse_qs
from urllib.parse import urlsplit

class TestURLField(BaseSeleniumTestCase):

    def test_url_after_click_search(self):
        search_url = "http://roboarchive.org/search"
        self.driver.get(search_url)

        button = self.wait_for_element("#search-button")
        button.click()

        self.wait_for_element('.search-result-item')

        url = "http://roboarchive.org/search?docdescription=false&doctitle=false&emptysearch=true&" \
              "fromdate=&gasrb=false&niab=false&page=1&search=&todate="

        sample_url_split         = urlsplit(url)
        sample_url_split_netloc  = sample_url_split.netloc
        sample_url_split_query   = sample_url_split.query
        sample_url_query_dict    = parse_qs(sample_url_split_query)

        current_url_split        = urlparse(self.driver.current_url)
        current_url_split_netloc = current_url_split.netloc
        current_url_split_query  = current_url_split.query
        current_url_query_dict   = parse_qs(current_url_split_query)

        self.assertEqual(sample_url_split_netloc, current_url_split_netloc)

        self.assertEqual(sample_url_query_dict, current_url_query_dict)

    def test_url_after_click_checkbox_NIAB_and_search(self):
        search_url = "http://roboarchive.org/search"
        self.driver.get(search_url)

        button = self.wait_for_element("#search-button")
        button.click()

        self.wait_for_element('.search-result-item')

        url = "http://roboarchive.org/search?docdescription=false&doctitle=false&emptysearch=true&" \
              "fromdate=&gasrb=false&niab=false&page=1&search=&todate="

        sample_url_parse = urlparse(url)
        current_url_parse = urlparse(self.driver.current_url)

        self.assertEqual(sample_url_parse, current_url_parse)

if __name__ == "__main__":
    unittest.main()
