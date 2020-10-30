import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.GlownaPage import GlownaPage


class TestBase(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.glowna_page = GlownaPage(cls.driver)
        cls.glowna_page.go_to_glowna_page()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
