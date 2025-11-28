import pytest
from utils.driver_utils import DriverUtils

@pytest.fixture(scope="function")
def driver():
    driver = DriverUtils.get_driver()
    yield driver
    driver.quit()
