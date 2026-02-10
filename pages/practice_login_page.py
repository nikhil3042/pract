from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.ID,'username')
    PASSWORD = (By.ID,'password')
    SUBMIT = (By.ID,'submit')

    def __init__(self,driver):
        super().__init__(driver)

    def enter_username(self,username):
        self.send_keys(self.USERNAME,username)
        self.logger.info(f'entered {username}')

    def enter_password(self,pwd):
        self.send_keys(self.PASSWORD,pwd)
        self.logger.info(f'entered password')

    def click_submit(self):
        self.click(self.SUBMIT)
        self.logger.info(f'clicked on submit')