from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from locators.courses_locators import CoursesLocators

class CoursesPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self, url: str):
        self.driver.get(url)

    def get_selenium_java_course_link(self):
        return self.driver.find_element(By.XPATH, CoursesLocators.COURSE_SELENIUM_JAVA)

    def click_selenium_java_course(self):
        self.get_selenium_java_course_link().click()

    def click_home_link(self):
        self.driver.find_element(By.XPATH, CoursesLocators.HOME_LINK).click()
    
    def click_practice_link(self):
        self.driver.find_element(By.XPATH, CoursesLocators.PRACTICE_LINK).click()

    def click_blog_link(self):
        self.driver.find_element(By.XPATH, CoursesLocators.BLOG_LINK).click()

    def click_contact_link(self):
        self.driver.find_element(By.XPATH, CoursesLocators.CONTACT_LINK).click()
