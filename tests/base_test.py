import pytest

class BaseTest:

    @pytest.fixture(autouse=True)
    def _setup(self, setup_and_teardown):
        self.driver = setup_and_teardown

# why i wrote this because from conftest setup and tear down ill get 'driver' and i have to call that
# fixture every test or should have the above method in every test method.
#so by doing this basetest setup i can auto use and call that driver here to use it in every test case