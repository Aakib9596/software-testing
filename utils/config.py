import os

BASE_URL = os.getenv("BASE_URL", "https://practicetestautomation.com/practice-test-login/")

LOGIN_URL = f"{BASE_URL}/practice-test-login/"
EXCEPTIONS_URL = f"{BASE_URL}/practice-test-exceptions/"
COURSES_URL = f"{BASE_URL}/courses/"
CONTACT_URL = f"{BASE_URL}/contact/"
BROWSER_TYPE = os.getenv("BROWSER_TYPE", "chromium") 

USER_USERNAME =os.getenv("USER_USERNAME", "student")
USER_PASSWORD =os.getenv("USER_PASSWORD", "Password123")    


