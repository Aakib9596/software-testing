
from pageobjects.login_page import LoginPage
from utils.config import BASE_URL, USER_USERNAME, USER_PASSWORD

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page(BASE_URL)
    login_page.enter_username(USER_USERNAME)
    login_page.enter_password(USER_PASSWORD)
    login_page.click_submit()
    
    assert "Logged In Successfully" in driver.title


