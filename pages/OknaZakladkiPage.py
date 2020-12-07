from locators.OknaZakladkiLocators import OknaZakladkiLocators
from pages.BasePage import BasePage
from pages.PodstawyPage import PodstawyPage
from log import log, for_all_methods


@for_all_methods(log)
class OknaZakladkiPage(OknaZakladkiLocators, BasePage):

    def otworz_podstawy_nowa_karta(self):
        self.find(self.PODSTAWY_KARTA).click()
        return PodstawyPage(self.driver)

    def otworz_podstawy_nowe_okno(self):
        self.find(self.PODSTAWY_OKNO).click()
        return PodstawyPage(self.driver)

    def powieksz_okno(self):
        self.driver.maximize_window()

    def przelacz_karte_lub_okno(self, numer):
        self.driver.switch_to.window(self.driver.window_handles[numer])
