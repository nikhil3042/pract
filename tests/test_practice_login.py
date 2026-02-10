import allure
import pytest

from pages.practice_login_page import LoginPage
from config.environment import Environment
from tests.base_test import BaseTest


@allure.feature('Login')
class TestLogin(BaseTest):

    @allure.title('TC_LOGIN_01 - Verify successful login')
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_login(self):
        env = Environment('practice')
        base_url = env.get_base_url()
        username = env.get_username()
        pwd = env.get_password()

        login = LoginPage(self.driver)

        with allure.step('enter creds and login'):
            login.navigate_to(base_url)
            login.enter_username(username)
            login.enter_password(pwd)
            login.click_submit()


