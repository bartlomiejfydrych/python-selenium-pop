from locators.WiecejRamekLocators import WiecejRamekLocators
from log import log, for_all_methods
from pages.BasePage import BasePage


@for_all_methods(log)
class WiecejRamekPage(WiecejRamekLocators, BasePage):

    # Metody formularza:
    def wpisz_imie(self, imie):
        self.find(self.IMIE_INPUT).send_keys(imie)

    def wpisz_nazwisko(self, nazwisko):
        self.find(self.NAZWISKO_INPUT).send_keys(nazwisko)

    def wpisz_email(self, email):
        self.find(self.EMAIL_INPUT).send_keys(email)

    def wpisz_miasto(self, miasto):
        self.find(self.MIASTO_INPUT).send_keys(miasto)

    def wpisz_ulica(self, ulica):
        self.find(self.ULICA_INPUT).send_keys(ulica)

    def akceptuj_regulamin(self):
        self.find(self.REGULAMIN_CHECKBOX).click()

    def wyslij_dane(self):
        self.find(self.WYSLIJ_BUTTON).click()

    def sprawdz_alert(self):
        assert self.find(self.GRATULACJE_ALERT).is_displayed()

    # Metody ramek:
    def przejdz_do_domyslnego_okna(self):
        self.driver.switch_to.default_content()

    def przejdz_do_iframe2(self):
        self.driver.switch_to.frame(self.find(self.IFRAME2))

    def przejdz_do_iframe3(self):
        self.driver.switch_to.frame(self.find(self.IFRAME3))

    def przejdz_do_iframe4(self):
        self.driver.switch_to.frame(self.find(self.IFRAME4))

    def przejdz_do_iframe5(self):
        self.driver.switch_to.frame(self.find(self.IFRAME5))

    def przejdz_do_parent_frame(self):
        self.driver.switch_to.parent_frame()
