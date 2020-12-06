from selenium.webdriver.support.select import Select

from configurations import TESTFILE_PATH
from locators.LokalizatoryLocators import LokalizatoryLocators
from log import log, for_all_methods
from pages.BasePage import BasePage


@for_all_methods(log)
class LokalizatoryPage(LokalizatoryLocators, BasePage):

    def wpisz_imie(self, imie):
        self.find(self.IMIE_INPUT).send_keys(imie)

    def wpisz_nazwisko(self, nazwisko):
        self.find(self.NAZWISKO_INPUT).send_keys(nazwisko)

    def wybierz_kraj(self, kraj_nazwa):
        select = Select(self.find(self.KRAJ_SELECT))
        select.select_by_visible_text(kraj_nazwa)

    def wybierz_jezyk(self, *jezyki):
        select = Select(self.find(self.JEZYK_SELECT))
        for jezyk_nazwa in jezyki:
            select.select_by_visible_text(jezyk_nazwa)

    def napisz_o_sobie(self, tekst):
        self.find(self.O_SOBIE_INPUT).send_keys(tekst)

    def wyslij_plik(self):
        self.find(self.PLIK_ZALACZNIK).send_keys(TESTFILE_PATH)

    def wybierz_plec(self, plec):
        if plec == "Mężczyzna":
            self.find(self.PLEC_MEZCZYZNA).click()
        elif plec == "Kobieta":
            self.find(self.PLEC_KOBIETA).click()
        elif plec == "Inne":
            self.find(self.PLEC_INNE).click()
        else:
            print("Źle podana płeć.")

    def akceptuj_regilamin(self):
        self.find(self.REGULAMIN_CHECKBOX).click()

    def wyslij_dane(self):
        self.find(self.WYSLIJ_BUTTON).click()

    def sprawdz_alert(self):
        assert self.find(self.GRATULACJE_ALERT).is_displayed()
