class ScrapeUseCase:
    def __init__(self, scraper, storage):
        self.scraper = scraper
        self.storage = storage

    def parse_data(self, raw_data):
        """
        Procesa los datos obtenidos del scraping.
        """
        return [item.text for item in raw_data]
