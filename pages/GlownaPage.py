from webdriver_manager import driver

from Locators.GlownaLocators import GlownaLocators
from pages.PodstawyPage import PodstawyPage


class GlownaPage(GlownaLocators):

    def __init__(self, driver):
        self.driver = driver

    def go_to_glowna_page(self):
        self.driver.get("http://dawidkaruga.pl/testerczaki/")
        return self

    def go_to_podstawy_page(self):
        self.driver.find_element(*self.PODSTAWY_ZACZNIJ).click()
        return PodstawyPage(driver)
