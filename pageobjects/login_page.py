from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from locators.login_locators import LoginLocators

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_login_page(self, url: str):
        self.driver.get(url)

    def enter_username(self, username: str):
        self.driver.find_element(By.XPATH, LoginLocators.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password: str):
        self.driver.find_element(By.XPATH, LoginLocators.PASSWORD_FIELD).send_keys(password)

    def click_submit(self):
        self.driver.find_element(By.XPATH, LoginLocators.SUBMIT_BUTTON).click()