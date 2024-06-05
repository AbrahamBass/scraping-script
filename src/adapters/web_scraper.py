
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By

class WebScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.logger = logging.getLogger(self.__class__.__name__)

    def find_by_tag(self):
        browser = webdriver.Firefox()
        browser.get('http://www.yahoo.com')
        elem = browser.find_element(By.TAG_NAME, 'p')
        self.logger.info("Data fetched successfully")
        return elem.text
        
    
