import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestLoginPage():

    @pytest.fixture()
    def setup(self):
        ser_obj = Service()
        self.driver = webdriver.Chrome(service=ser_obj)

        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        yield
        self.driver.close()

    def test_homepage(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
       # self.driver.get_screenshot_as_file("C:\capture\img0.png")
        assert self.driver.title == "OrangeHRM"
        time.sleep(5)

    def test_login(self, setup):
        # Login
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.TAG_NAME, "button").click()
        assert self.driver.title == "OrangeHRM"
       # self.driver.get_screenshot_as_file("C:\capture\img1.jpg")
        time.sleep(5)
