import pytest
from pageobjects.courses_page import CoursesPage
from utils.config import COURSES_URL

def test_courses_page_title(driver):
    courses_page = CoursesPage(driver)
    courses_page.open(COURSES_URL)
    
    # Verify Page Title
    assert "Courses | Practice Test Automation" in driver.title

def test_selenium_java_course_present(driver):
    courses_page = CoursesPage(driver)
    courses_page.open(COURSES_URL)
    
    # Verify Course is present
    course_link = courses_page.get_selenium_java_course_link()
    assert course_link.is_displayed()
    assert "Selenium WebDriver: Selenium Automation Testing with Java" in course_link.text

def test_navigate_to_course_details(driver):
    courses_page = CoursesPage(driver)
    courses_page.open(COURSES_URL)
    
    # Click on the course
    courses_page.click_selenium_java_course()
    
    # Check if a new tab is opened
    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[-1])
    
    # Verify navigation to the course page (URL or Title)
    # The URL should contain 'beginners-course-coupon' based on subagent findings, 
    # or at least change from the courses page.
    assert "udemy.com" in driver.current_url or "selenium-for-beginners" in driver.current_url

def test_header_navigation(driver):
    courses_page = CoursesPage(driver)
    courses_page.open(COURSES_URL)
    
    # Click Home and verify
    courses_page.click_home_link()
    assert "Practice Test Automation" in driver.title
    assert driver.current_url == "https://practicetestautomation.com/"
