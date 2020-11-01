from locators.GlownaLocators import GlownaLocators
from pages.AsercjaPage import AsercjaPage
from pages.PodstawyPage import PodstawyPage
from pages.WiecejElementowPage import WiecejElementowPage


class GlownaPage(GlownaLocators):

    def __init__(self, driver):
        self.driver = driver

    def go_to_glowna_page(self):
        self.driver.get("http://dawidkaruga.pl/testerczaki/")
        return self

    def go_to_podstawy_page(self):
        self.driver.find_element(*self.PODSTAWY_ZACZNIJ).click()
        return PodstawyPage(self.driver)

    def go_to_wiecej_elementow_page(self):
        self.driver.find_element(*self.WIECEJ_ELEMENTOW_ZACZNIJ).click()
        return WiecejElementowPage(self.driver)

    def go_to_asercja_page(self):
        self.driver.find_element(*self.ASERCJA_ZACZNIJ).click()
        return AsercjaPage(self.driver)
