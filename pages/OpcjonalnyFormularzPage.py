from selenium.webdriver.support import expected_conditions as ec

from locators.OpcjonalnyFormularzLocators import OpcjonalnyFormularzLocators
from log import for_all_methods, log
from pages.BasePage import BasePage


@for_all_methods(log)
class OpcjonalnyFormularzPage(OpcjonalnyFormularzLocators, BasePage):

    def wpisz_imie(self, imie):
        self.find(self.IMIE_INPUT).send_keys(imie)

    def wpisz_nazwisko(self, nazwisko):
        self.find(self.NAZWISKO_INPUT).send_keys(nazwisko)

    def wpisz_email(self, email):
        self.find(self.EMAIL_INPUT).send_keys(email)

    def dodatkowe_pola_kliknij(self):
        self.find(self.DODATKOWE_POLA_CHECKBOX).click()

    def wpisz_miasto(self, miasto):
        self.wait.until(ec.visibility_of_element_located(self.MIASTO_INPUT))
        self.find(self.MIASTO_INPUT).send_keys(miasto)

    def wpisz_ulica(self, ulica):
        self.wait.until(ec.visibility_of_element_located(self.ULICA_INPUT))
        self.find(self.ULICA_INPUT).send_keys(ulica)

    def wyslij_dane(self):
        self.find(self.WYSLIJ_BUTTON).click()

    def sprawdz_alert(self):
        assert self.find(self.GRATULACJE_ALERT).is_displayed()
