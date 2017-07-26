from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://roboarchive.org/search")
assert "Robo Archive" in driver.title
elem = driver.find_element_by_id("search-input")
elem.send_keys("Уфа")
elem.send_keys(Keys.RETURN)