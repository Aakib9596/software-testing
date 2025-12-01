import pytest
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
    InvalidElementStateException,
    StaleElementReferenceException,
    TimeoutException
)
from selenium.webdriver.common.by import By
from pageobjects.exceptions_page import ExceptionsPage
from locators.exceptions_locators import ExceptionsLocators
from utils.config import EXCEPTIONS_URL

@pytest.mark.usefixtures("driver")
def test_no_such_element_exception(driver):
    """Test NoSuchElementException is raised when element is not found."""
    exceptions_page = ExceptionsPage(driver)
    exceptions_page.open(EXCEPTIONS_URL)
    with pytest.raises(NoSuchElementException):
        driver.find_element(By.XPATH, ExceptionsLocators.ROW_2_INPUT)

@pytest.mark.usefixtures("driver")
def test_element_not_interactable_exception(driver):
    """Test ElementNotInteractableException is raised for disabled element."""
    exceptions_page = ExceptionsPage(driver)
    exceptions_page.open(EXCEPTIONS_URL)
    exceptions_page.click_add_button()
    exceptions_page.wait_for_row_2_input()
    row_1_input = exceptions_page.get_row_1_input_element()
    with pytest.raises(ElementNotInteractableException):
        row_1_input.send_keys("Test")

@pytest.mark.usefixtures("driver")
def test_invalid_element_state_exception(driver):
    """Test InvalidElementStateException is raised when clearing a disabled input."""
    exceptions_page = ExceptionsPage(driver)
    exceptions_page.open(EXCEPTIONS_URL)
    row_1_input = exceptions_page.get_row_1_input_element()
    assert not row_1_input.is_enabled()
    with pytest.raises(InvalidElementStateException):
        row_1_input.clear()

@pytest.mark.usefixtures("driver")
def test_stale_element_reference_exception(driver):
    """Test StaleElementReferenceException is raised for a stale element."""
    exceptions_page = ExceptionsPage(driver)
    exceptions_page.open(EXCEPTIONS_URL)
    instructions = exceptions_page.get_instructions_element()
    exceptions_page.wait_for_row_2_input()
    with pytest.raises(StaleElementReferenceException):
        instructions.text

@pytest.mark.usefixtures("driver")
def test_timeout_exception(driver):
    """Test TimeoutException is raised when waiting for an element that doesn't appear in time."""
    exceptions_page = ExceptionsPage(driver)
    exceptions_page.open(EXCEPTIONS_URL)
    exceptions_page.click_add_button()
    with pytest.raises(TimeoutException):
        exceptions_page.wait_for_row_2_input(timeout=3)
