import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from entities.source_model import TextAlone
from selenium.common.exceptions import NoSuchElementException, WebDriverException

def SeleniumBrowser():
    options = webdriver.EdgeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    return webdriver.Edge(options=options)
    

class WebScraper:
    def __init__(self, base_url):
        self.base_url = base_url 
        self.logger = logging.getLogger(self.__class__.__name__)

    def find_by_tag(self, tag: str):
        browser = SeleniumBrowser()
        try:
            browser.get('https://portfolio-abrahambass.vercel.app/')
        except WebDriverException as e:
            err = f"Please enter the complete and correctly formatted URL. The URL you provided seems to be invalid."
            self.logger.error(err)
            raise Exception(err)    
        except Exception as e: 
            err = f"An unexpected error occurred. Please try again later."
            self.logger.error(err)
            raise Exception(err)

        try:
            elems = browser.find_elements(By.TAG_NAME, tag)
            self.logger.info("Data fetched successfully")
            arrList = list()
            for e in elems:
                arrList.append(
                    TextAlone(
                        title=e.text,
                        id=e.get_attribute("id"),
                        className=e.get_attribute("class")
                    )
                )
            return arrList
        except NoSuchElementException as e: 
            err = f"no such element"
            self.logger.error(err)
            raise Exception(err) 
        
    
