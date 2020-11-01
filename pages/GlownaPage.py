from locators.GlownaLocators import GlownaLocators
from pages.AsercjaPage import AsercjaPage
from pages.LokalizatoryPage import LokalizatoryPage
from pages.PodstawyPage import PodstawyPage
from pages.UkryteElementyPage import UkryteElementyPage
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

    def go_to_lokalizatory_page(self):
        self.driver.find_element(*self.LOKALIZATORY_ZACZNIJ).click()
        return LokalizatoryPage(self.driver)

    def go_to_ukryte_elementy_page(self):
        self.driver.find_element(*self.UKRYTE_ELEMENTY_ZACZNIJ).click()
        return UkryteElementyPage(self.driver)