from locators.GlownaLocators import GlownaLocators
from log import log, for_all_methods
from pages.AsercjaPage import AsercjaPage
from pages.BasePage import BasePage
from pages.KliknijPrzytrzymajPage import KliknijPrzytrzymajPage
from pages.KomunikatyPage import KomunikatyPage
from pages.LokalizatoryPage import LokalizatoryPage
from pages.MenuPage import MenuPage
from pages.NiestandardoweListyPage import NiestandardoweListyPage
from pages.OknaZakladkiPage import OknaZakladkiPage
from pages.OpcjonalnyFormularzPage import OpcjonalnyFormularzPage
from pages.PodstawyPage import PodstawyPage
from pages.PrzeciagnijUpuscPage import PrzeciagnijUpuscPage
from pages.RamkaPage import RamkaPage
from pages.TabelePage import TabelePage
from pages.UkryteElementyPage import UkryteElementyPage
from pages.WiecejElementowPage import WiecejElementowPage
from pages.WiecejRamekPage import WiecejRamekPage


@for_all_methods(log)
class GlownaPage(GlownaLocators, BasePage):

    def go_to_glowna_page(self):
        self.driver.get("http://dawidkaruga.pl/testerczaki/")
        return self

    def go_to_podstawy_page(self):
        self.find(self.PODSTAWY_ZACZNIJ).click()
        return PodstawyPage(self.driver)

    def go_to_wiecej_elementow_page(self):
        self.find(self.WIECEJ_ELEMENTOW_ZACZNIJ).click()
        return WiecejElementowPage(self.driver)

    def go_to_asercja_page(self):
        self.find(self.ASERCJA_ZACZNIJ).click()
        return AsercjaPage(self.driver)

    def go_to_lokalizatory_page(self):
        self.find(self.LOKALIZATORY_ZACZNIJ).click()
        return LokalizatoryPage(self.driver)

    def go_to_ukryte_elementy_page(self):
        self.find(self.UKRYTE_ELEMENTY_ZACZNIJ).click()
        return UkryteElementyPage(self.driver)

    def go_to_opcjonalny_formularz_page(self):
        self.find(self.OPCJONALNY_FORMULARZ_ZACZNIJ).click()
        return OpcjonalnyFormularzPage(self.driver)

    def go_to_ramka_page(self):
        self.find(self.RAMKA_ZACZNIJ).click()
        return RamkaPage(self.driver)

    def go_to_wiecej_ramek_page(self):
        self.find(self.WIECEJ_RAMEK_ZACZNIJ).click()
        return WiecejRamekPage(self.driver)

    def go_to_okna_zakladki_page(self):
        self.find(self.OKNA_ZAKLADKI_ZACZNIJ).click()
        return OknaZakladkiPage(self.driver)

    def go_to_komunikaty_page(self):
        self.find(self.KOMUNIKATY_ZACZNIJ).click()
        return KomunikatyPage(self.driver)

    def go_to_menu_page(self):
        self.find(self.MENU_ZACZNIJ).click()
        return MenuPage(self.driver)

    def go_to_przeciagnij_upusc_page(self):
        self.find(self.PRZECIAGNIJ_UPUSC_ZACZNIJ).click()
        return PrzeciagnijUpuscPage(self.driver)

    def go_to_kliknij_przytrzymaj_page(self):
        self.find(self.KLIKNIJ_PRZYTRZYMAJ_ZACZNIJ).click()
        return KliknijPrzytrzymajPage(self.driver)

    def go_to_niestandardowe_listy_page(self):
        self.find(self.NIESTANDARDOWE_LISTY_ZACZNIJ).click()
        return NiestandardoweListyPage(self.driver)

    def go_to_tabele_page(self):
        self.find(self.TABELE_ZACZNIJ).click()
        return TabelePage(self.driver)
