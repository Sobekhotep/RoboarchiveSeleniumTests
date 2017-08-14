import unittest

from urllib.parse import urlparse
from urllib.parse import parse_qs
from urllib.parse import urlsplit

from base_selenium_test_case import BaseSeleniumTestCase

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

        click_search_options = self.wait_for_element(".extended-search")
        button = self.wait_for_element(".extended-search")
        button.click()

        click_search_options_niab = self.wait_for_element(".col-sm-8")
        button = self.wait_for_element(".col-sm-8>div.checkbox:nth-child(1)>label>input[type=checkbox]")
        button.click()

        button = self.wait_for_element("#search-button")
        button.click()

        self.wait_for_element('.search-result-item')

        url = "http://roboarchive.org/search?docdescription=false&doctitle=false&emptysearch=true&/" \
              "fromdate=&gasrb=false&niab=true&page=1&search=&todate="

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

    def test_url_after_click_checkbox_ZGIARB_and_search(self):

        search_url = "http://roboarchive.org/search"
        self.driver.get(search_url)

        click_search_options = self.wait_for_element(".extended-search")
        button = self.wait_for_element(".extended-search")
        button.click()

        click_search_options_zgia_rb = self.wait_for_element(".col-sm-8")
        button = self.wait_for_element(".col-sm-8>div.checkbox:nth-child(2)>label>input[type=checkbox]")
        button.click()

        button = self.wait_for_element("#search-button")
        button.click()

        self.wait_for_element('.search-result-item')

        url = "http://roboarchive.org/search?docdescription=false&doctitle=false&emptysearch=true&/" \
              "fromdate=&gasrb=true&niab=false&page=1&search=&todate="

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

    def test_url_after_click_checkbox_document_header_and_search(self):

        search_url = "http://roboarchive.org/search"
        self.driver.get(search_url)

        click_search_options = self.wait_for_element(".extended-search")
        button = self.wait_for_element(".extended-search")
        button.click()

        click_search_options_document_header = self.wait_for_element(".col-sm-8")
        button = self.wait_for_element(".form-group:nth-child(2)>.col-sm-8>div.checkbox:nth-child(1)>label>input[type=checkbox]")
        button.click()

        button = self.wait_for_element("#search-button")
        button.click()

        self.wait_for_element('.search-result-item')

        url = "http://roboarchive.org/search?docdescription=false&doctitle=true&emptysearch=true&/" \
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

    def test_url_after_click_checkbox_document_description_and_search(self):

        search_url = "http://roboarchive.org/search"
        self.driver.get(search_url)

        click_search_options = self.wait_for_element(".extended-search")
        button = self.wait_for_element(".extended-search")
        button.click()

        click_search_options_document_description = self.wait_for_element(".col-sm-8")
        button = self.wait_for_element(".form-group:nth-child(2)>.col-sm-8>div.checkbox:nth-child(2)>label>input[type=checkbox]")
        button.click()

        button = self.wait_for_element("#search-button")
        button.click()

        self.wait_for_element('.search-result-item')

        url = "http://roboarchive.org/search?docdescription=true&doctitle=false&emptysearch=true&\
        fromdate=&gasrb=false&niab=false&page=1&search=&todate="

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

    def test_url_after_enter_value_in_time_range_fields(self):

        search_url = "http://roboarchive.org/search"
        self.driver.get(search_url)

        click_search_options = self.wait_for_element(".extended-search")
        button = self.wait_for_element(".extended-search")
        button.click()

        click_search_options_time_range_from = self.wait_for_element(".col-sm-8")
        elem = self.wait_for_element(".form-group:nth-child(3)>.col-sm-8>.input-group>#dateRangeSelector")
        elem.send_keys(1800)

        button = self.wait_for_element("#search-button")
        button.click()

        self.wait_for_element('.search-result-item')

        url = "http://roboarchive.org/search?docdescription=false&doctitle=false&emptysearch=true&fromdate=1800&gasrb=false&niab=false&page=1&search=&todate="

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

    def test_url_after_enter_value_ufa_in_search_field(self):

        search_url = "http://roboarchive.org/search"
        self.driver.get(search_url)

        click_search_options_time_range_from = self.wait_for_element("#search-input")
        elem = self.wait_for_element("#search-input")
        elem.send_keys("Уфа")

        button = self.wait_for_element("#search-button")
        button.click()

        self.wait_for_element('.search-result-item')

        url = "http://roboarchive.org/search?docdescription=false&doctitle=false&emptysearch=true&\
        fromdate=&gasrb=false&niab=false&page=1&search=%D0%A3%D1%84%D0%B0&todate="

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

    def test_url_after_enter_complex_values(self):

        search_url = "http://roboarchive.org/search"
        self.driver.get(search_url)

        click_search_options_time_range_from = self.wait_for_element("#search-input")
        elem = self.wait_for_element("#search-input")
        elem.send_keys("Уфа")

        click_search_options = self.wait_for_element(".extended-search")
        button = self.wait_for_element(".extended-search")
        button.click()

        click_search_options_zgia_rb = self.wait_for_element(".col-sm-8")
        button = self.wait_for_element(".col-sm-8>div.checkbox:nth-child(2)>label>input[type=checkbox]")
        button.click()

        click_search_options_time_range_from = self.wait_for_element(".col-sm-8")
        elem = self.wait_for_element(".form-group:nth-child(3)>.col-sm-8>.input-group>#dateRangeSelector")
        elem.send_keys(1800)

        button = self.wait_for_element("#search-button")
        button.click()

        self.wait_for_element('.search-result-item')

        url = "http://roboarchive.org/search?docdescription=false&doctitle=false&emptysearch=true&fromdate=1800&gasrb=true&niab=false&page=1&search=%D0%A3%D1%84%D0%B0&todate="

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

if __name__ == "__main__":
    unittest.main()
