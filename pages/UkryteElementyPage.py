from locators.UkryteElementyLocators import UkryteElementyLocators
from log import log, for_all_methods
from pages.BasePage import BasePage


@for_all_methods(log)
class UkryteElementyPage(UkryteElementyLocators, BasePage):

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
