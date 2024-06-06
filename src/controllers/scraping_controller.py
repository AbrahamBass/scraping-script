from adapters.web_scraper import WebScraper
from adapters.data_storage import DataStorage
from usecases.scrape_usecase import ScrapeUseCase
from entities.source_model import TextAlone
import logging
import os
import platform

def ClearConsole():
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

class ScrapingController:
    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)

    def run(self):

        scraper = WebScraper(self.config.BASE_URL)
        storage = DataStorage(self.config.DATA_PATH)
        usecase = ScrapeUseCase(scraper, storage)
        
        while True:
            print("ScrapiApi...")
            print("1: Buscar por etiquetas\n2: Buscar por selector\n3: Caturar screenshot\n4: Salir")
            action = input("¿Qué acción deseas realizar? ").strip().lower()
            if action == "1":
                tag = input("Introduce la etiqueta a buscar: ").strip()
                print("Cargando...")
                try:
                    raw_data: list[TextAlone] = scraper.find_by_tag(tag=tag)
                    print("Terminado...")
                    for e in raw_data:
                        print(f"{e.title} - {e.id} - {e.className}")
                    input("Presione cualquier tecla para continuar... ")
                    ClearConsole()
                except Exception as e:
                    print(e.args)
                    continue 
            elif action == "4":
                ClearConsole()
                print("Saliendo del programa...")
                break
                    
