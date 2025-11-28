from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.exceptions_locators import ExceptionsLocators

class ExceptionsPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self, url: str):
        self.driver.get(url)

    def click_add_button(self):
        self.driver.find_element(By.XPATH, ExceptionsLocators.ADD_BUTTON).click()

    def click_edit_button(self):
        self.driver.find_element(By.XPATH, ExceptionsLocators.ROW_1_EDIT_BUTTON).click()

    def get_row_1_input_element(self):
        return self.driver.find_element(By.XPATH, ExceptionsLocators.ROW_1_INPUT)

    def get_instructions_element(self):
        return self.driver.find_element(By.XPATH, ExceptionsLocators.INSTRUCTIONS)

    def wait_for_row_2_input(self, timeout: int = 10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located((By.XPATH, ExceptionsLocators.ROW_2_INPUT)))
    
    def is_row_2_displayed(self):
        try:
            return self.driver.find_element(By.XPATH, ExceptionsLocators.ROW_2_INPUT).is_displayed()
        except:
            return False
