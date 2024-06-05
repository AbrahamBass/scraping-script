from adapters.web_scraper import WebScraper
from adapters.data_storage import DataStorage
from usecases.scrape_usecase import ScrapeUseCase
import logging

class ScrapingController:
    def __init__(self, config):
        self.config = config

    def run(self):
        """
        Ejecuta el proceso de scraping.
        """

        scraper = WebScraper(self.config.BASE_URL)
        storage = DataStorage(self.config.DATA_PATH)
        usecase = ScrapeUseCase(scraper, storage)
        
        while True:
            print("¿Qué acción deseas realizar?")
            print("1: Buscar por etiquetas")
            action = input("¿Qué acción deseas realizar? (scrape/save/exit): ").strip().lower()

            if action == "1":
                raw_data = scraper.find_by_tag()
                print(raw_data)
