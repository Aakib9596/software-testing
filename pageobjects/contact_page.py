from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.contact_locators import ContactLocators

class ContactPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self, url: str):
        self.driver.get(url)

    def enter_first_name(self, first_name: str):
        self.driver.find_element(By.XPATH, ContactLocators.FIRST_NAME).send_keys(first_name)

    def enter_last_name(self, last_name: str):
        self.driver.find_element(By.XPATH, ContactLocators.LAST_NAME).send_keys(last_name)

    def enter_email(self, email: str):
        self.driver.find_element(By.XPATH, ContactLocators.EMAIL).send_keys(email)

    def enter_message(self, message: str):
        self.driver.find_element(By.XPATH, ContactLocators.MESSAGE).send_keys(message)

    def click_submit(self):
        self.driver.find_element(By.XPATH, ContactLocators.SUBMIT_BUTTON).click()

    def get_first_name_field(self):
        return self.driver.find_element(By.XPATH, ContactLocators.FIRST_NAME)

    def get_email_field(self):
        return self.driver.find_element(By.XPATH, ContactLocators.EMAIL)

    def is_success_message_displayed(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, ContactLocators.SUCCESS_MESSAGE)))
            return True
        except:
            return False

    def get_success_message_text(self):
        return self.driver.find_element(By.XPATH, ContactLocators.SUCCESS_MESSAGE).text
