import pytest
from pageobjects.contact_page import ContactPage
from utils.config import CONTACT_URL

def test_contact_page_title(driver):
    contact_page = ContactPage(driver)
    contact_page.open(CONTACT_URL)
    assert "Contact" in driver.title

def test_submit_valid_contact_form(driver):
    contact_page = ContactPage(driver)
    contact_page.open(CONTACT_URL)
    
    contact_page.enter_first_name("John")
    contact_page.enter_last_name("Doe")
    contact_page.enter_email("john.doe@example.com")
    contact_page.enter_message("This is a test message for automation testing.")
    contact_page.click_submit()
    
    assert contact_page.is_success_message_displayed()

def test_submit_form_without_first_name(driver):
    contact_page = ContactPage(driver)
    contact_page.open(CONTACT_URL)
    
    contact_page.enter_last_name("Doe")
    contact_page.enter_email("john.doe@example.com")
    contact_page.enter_message("Test message")
    contact_page.click_submit()
    
    first_name_field = contact_page.get_first_name_field()
    validation_message = first_name_field.get_attribute("validationMessage")
    assert validation_message is not None

def test_submit_form_with_invalid_email(driver):
    contact_page = ContactPage(driver)
    contact_page.open(CONTACT_URL)
    
    contact_page.enter_first_name("John")
    contact_page.enter_last_name("Doe")
    contact_page.enter_email("invalid-email")
    contact_page.enter_message("Test message")
    contact_page.click_submit()
    
    email_field = contact_page.get_email_field()
    validation_message = email_field.get_attribute("validationMessage")
    assert validation_message is not None

def test_all_form_fields_are_displayed(driver):
    contact_page = ContactPage(driver)
    contact_page.open(CONTACT_URL)
    
    assert contact_page.get_first_name_field().is_displayed()
    assert contact_page.get_email_field().is_displayed()
