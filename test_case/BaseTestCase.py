from selenium import webdriver
import unittest2
import time


class BaseTestCase(unittest2.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()


    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()

