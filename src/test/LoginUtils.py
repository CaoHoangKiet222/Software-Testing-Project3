import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "http://localhost/moodle/login/index.php"


class LUtils:
    @staticmethod
    def login(username, password):
        driver.get(url)
        driver.find_element(By.ID, "username").clear()
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "loginbtn").click()

    @staticmethod
    def logout():
        userMenu = driver.find_element(By.ID, "user-menu-toggle")
        if userMenu.is_displayed():
            userMenu.click()
            driver.find_element(
                By.XPATH,
                "//a[starts-with(@href, 'http://localhost/moodle/login/logout.php')]",
            ).click()
            time.sleep(2)
