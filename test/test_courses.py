import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from pageobjects.courses_page import CoursesPage
from utils.config import COURSES_URL

@pytest.mark.usefixtures("driver")
def test_courses_page_title(driver: WebDriver):
    """Verify the Courses page title."""
    courses_page = CoursesPage(driver)
    courses_page.open(COURSES_URL)
    assert "Courses | Practice Test Automation" in driver.title

def test_selenium_java_course_present(driver: WebDriver):
    """Check if Selenium Java course is present on the Courses page."""
    courses_page = CoursesPage(driver)
    courses_page.open(COURSES_URL)
    course_link = courses_page.get_selenium_java_course_link()
    assert course_link.is_displayed()
    assert "Selenium WebDriver: Selenium Automation Testing with Java" in course_link.text

@pytest.mark.usefixtures("driver")
def test_navigate_to_course_details(driver: WebDriver):
    """Verify navigation to the Selenium Java course details page."""
    courses_page = CoursesPage(driver)
    courses_page.open(COURSES_URL)
    courses_page.click_selenium_java_course()
    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[-1])
    assert "udemy.com" in driver.current_url or "selenium-for-beginners" in driver.current_url

def test_header_navigation(driver: WebDriver):
    """Verify Home navigation from the Courses page header."""
    courses_page = CoursesPage(driver)
    courses_page.open(COURSES_URL)
    courses_page.click_home_link()
    assert "Practice Test Automation" in driver.title
    assert driver.current_url == "https://practicetestautomation.com/"
