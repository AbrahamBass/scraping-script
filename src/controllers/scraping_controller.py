from adapters.web_scraper import WebScraper
from adapters.data_storage import DataStorage
from usecases.scrape_usecase import ScrapeUseCase
from entities.source_model import TextAlone
from selenium.webdriver.common.by import By
from methods.scraping_method import ClearConsole
import logging

class ScrapingController:
    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)

    def run(self):

        scraper = WebScraper()
        storage = DataStorage(self.config.DATA_PATH)
        usecase = ScrapeUseCase(scraper, storage)

        while True:
            print("- SCRAPIAPI ->")
            print("- 1 BUSCAR POR ETIQUETA ->\n- 2 BUSCAR POR SELECTOR ->\n- 3 SCREENSHOT ->\n- 4 SALIR ->")
            action = input("¿QUE ACCION DESEA REALIZAR? -> ").strip()

            if action != "4":
                page = input("- INGRESE LA URL DE LA WEB -> ").strip()

            if action == "1":
                tag = input("INTRODUCE LA ETIQUETA A BUSCAR -> ").strip()
                print("CARGANDO...") 
                try:
                    raw_data: list[TextAlone] = scraper.find_all(By.TAG_NAME, page,tag)
                    usecase.parse_data(raw_data)
                except Exception as e:
                    print(e.args)
                    continue
            elif action == "2":
                selector = input("INTRODUCE EL SELECTOR A BUSCAR -> ").strip()
                print("CARGANDO...") 
                try:
                    raw_data: list[TextAlone] = scraper.find_all(By.CSS_SELECTOR, page,selector)
                    usecase.parse_data(raw_data)
                except Exception as e:
                    print(e.args)
                    continue
            elif action == "3":
                print("CARGANDO...")
                try:
                    message: str = scraper.screenshot(page)
                    print(message)
                except Exception as e:
                    print(e.args)
                    continue
            elif action == "4":
                ClearConsole()
                self.logger.info("User selected 'Salir'")
                break
