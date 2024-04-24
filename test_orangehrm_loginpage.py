import pytest
import time
import mysql.connector
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from BaseClass import BaseClass


class TestLoginPage(BaseClass):

    @pytest.fixture()
    def setup(self):
        ser_obj = Service()
        self.driver = webdriver.Chrome(service=ser_obj)

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        self.driver.close()

    def test_homepage(self, setup):
        log = self.getLogger()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        log.debug("*****************************OrangeHRM-Testcase001******************")
        assert self.driver.title == "OrangeHRM"
        self.driver.save_screenshot(".\\screenshot\\"+"loginPageTitle.png")
        log.debug("***********Verify the Title of Login Page**************")
        time.sleep(5)

    def test_login(self, setup):
        log = self.getLogger()
        log.debug("*****************************OrangeHRM-Testcase002******************")
        # Database connection
        try:
            con = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="root", database="orangehrm")
            curs = con.cursor()  # create cursor
            curs.execute("select * from user_login_password")  # execute query through cursor
            for row in curs:
                self.driver.get("https://opensource-demo.orangehrmlive.com/")
                self.driver.find_element(By.NAME, "username").send_keys(row[1])
                self.driver.find_element(By.NAME, "password").send_keys(row[2])
                self.driver.find_element(By.TAG_NAME, "button").click()
                time.sleep(5)
                # validation
                if self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index":
                    time.sleep(5)
                    # print("test passed")
                    log.debug("********************Successfully login*****************")
                else:
                    # print("test failed")
                    self.driver.save_screenshot(".\\screenshot\\"+"Invalid_Credentials.png")
                    log.error("*******************Invalid Credentials**********************")

            self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
            time.sleep(5)
            con.close()
        except:
            log.error("**********************Database connection unsuccessful....***************")
        log.info("**************Finished....*************")

