from selenium import webdriver
from utils.logger import get_logger

logger = get_logger(__name__)

class DriverManager:
    @staticmethod
    def get_driver(browser: str):
        browser = browser.lower()

        if browser == "chrome":
            logger.info("Initializing Chrome browser")
            chrome_driver = webdriver.Chrome()
            chrome_driver.maximize_window()
            return chrome_driver

        elif browser == "edge":
            logger.info("Initializing Edge browser")
            edge_driver = webdriver.Edge()
            edge_driver.maximize_window()
            return edge_driver

        else:
            raise ValueError(f"Browser '{browser}' is not supported. Use chrome or edge.")
