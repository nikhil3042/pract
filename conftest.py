import pytest
from utils.driver_manager import DriverManager
from utils.logger import get_logger

logger = get_logger(__name__)

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests (chrome or edge)"
    )

@pytest.fixture()
def setup_and_teardown(request):
    browser = request.config.getoption("--browser") #It reads the value passed from the pytest command line.

    logger.info(f"Launching browser: {browser}")
    driver = DriverManager.get_driver(browser)

    yield driver

    logger.info("Closing browser")
    driver.quit()

