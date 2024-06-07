from entities.source_model import TextAlone
from methods.scraping_method import ClearConsole

class ScrapeUseCase:
    def __init__(self, scraper, storage):
        self.scraper = scraper
        self.storage = storage

    def parse_data(self, raw_data: list[TextAlone]):
        print("TERMINADO...")
        for e in raw_data:
            print(f"{e.title} - {e.id} - {e.className}")
        input("Presione cualquier tecla para continuar... ")
        ClearConsole()
