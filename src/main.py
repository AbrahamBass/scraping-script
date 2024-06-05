import argparse
import logging
from config import Config
from controllers.scraping_controller import ScrapingController


def main():
    parser = argparse.ArgumentParser(description="Script de web scraping.")
    parser.add_argument('--base_url', type=str, default="https://example.com", help='URL base para el scraping')
    parser.add_argument('--data_path', type=str, default="data/processed/data.json", help='Ruta para guardar los datos')
    parser.add_argument('--log_path', type=str, default="logs/scraping.log", help='Ruta para guardar los logs')
    args = parser.parse_args()

    logging.basicConfig(filename=args.log_path, level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    config = Config(args.base_url, args.data_path, args.log_path)
    controller = ScrapingController(config)
    controller.run()


if __name__ == "__main__":
    main()
