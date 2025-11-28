import pytest
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
    InvalidElementStateException,
    StaleElementReferenceException,
    TimeoutException
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobjects.exceptions_page import ExceptionsPage
from locators.exceptions_locators import ExceptionsLocators
from utils.config import EXCEPTIONS_URL

def test_no_such_element_exception(driver):
    exceptions_page = ExceptionsPage(driver)
    exceptions_page.open(EXCEPTIONS_URL)
    with pytest.raises(NoSuchElementException):
        driver.find_element(By.XPATH, ExceptionsLocators.ROW_2_INPUT)

def test_element_not_interactable_exception(driver):
    exceptions_page = ExceptionsPage(driver)
    exceptions_page.open(EXCEPTIONS_URL)
    

    exceptions_page.click_add_button()
    
    # Wait for Row 2 to appear (it takes time)
    exceptions_page.wait_for_row_2_input()
    row_1_input = exceptions_page.get_row_1_input_element()
    
    # Trying to send keys to a disabled element
    with pytest.raises(ElementNotInteractableException):
        row_1_input.send_keys("Test")

def test_invalid_element_state_exception(driver):
    exceptions_page = ExceptionsPage(driver)
    exceptions_page.open(EXCEPTIONS_URL)
    row_1_input = exceptions_page.get_row_1_input_element()
    
    # Verify it's disabled
    assert not row_1_input.is_enabled()
    
    # Try to clear it
    with pytest.raises(InvalidElementStateException):
        row_1_input.clear()

def test_stale_element_reference_exception(driver):
    exceptions_page = ExceptionsPage(driver)
    exceptions_page.open(EXCEPTIONS_URL)
    instructions = exceptions_page.get_instructions_element()
    exceptions_page.wait_for_row_2_input()
    with pytest.raises(StaleElementReferenceException):
        instructions.text

def test_timeout_exception(driver):
    exceptions_page = ExceptionsPage(driver)
    exceptions_page.open(EXCEPTIONS_URL)
    exceptions_page.click_add_button()

    with pytest.raises(TimeoutException):
        exceptions_page.wait_for_row_2_input(timeout=3)
