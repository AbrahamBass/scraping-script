import json
import os
import logging

class DataStorage:
    def __init__(self, data_path):
        self.data_path = data_path
        self.logger = logging.getLogger(self.__class__.__name__)

    def save_data(self, data):
        """
        Guarda los datos en el archivo especificado.
        """
        self.logger.info(f"Saving data to {self.data_path}")
        try:
            os.makedirs(os.path.dirname(self.data_path), exist_ok=True)
            with open(self.data_path, 'w') as f:
                json.dump(data, f)
            self.logger.info("Data saved successfully")
        except Exception as e:
            self.logger.error(f"Error saving data: {e}")
