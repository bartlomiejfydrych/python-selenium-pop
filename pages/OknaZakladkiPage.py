from locators.OknaZakladkiLocators import OknaZakladkiLocators
from pages.PodstawyPage import PodstawyPage


class OknaZakladkiPage(OknaZakladkiLocators):

    def __init__(self, driver):
        self.driver = driver

    def otworz_podstawy_nowa_karta(self):
        self.driver.find_element(*self.PODSTAWY_KARTA).click()
        return PodstawyPage(self.driver)

    def otworz_podstawy_nowe_okno(self):
        self.driver.find_element(*self.PODSTAWY_OKNO).click()
        return PodstawyPage(self.driver)

    def powieksz_okno(self):
        self.driver.maximize_window()

    def przelacz_karte_lub_okno(self, numer):
        self.driver.switch_to.window(self.driver.window_handles[numer])
