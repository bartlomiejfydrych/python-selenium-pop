from locators.NiestandardoweListyLocators import NiestandardoweListyLocators
from log import log, for_all_methods
from pages.BasePage import BasePage


@for_all_methods(log)
class NiestandardoweListyPage(NiestandardoweListyLocators, BasePage):

    # Metody zadania 1:
    def z1_kliknij_wybierz_button(self):
        self.find(self.Z1_WYBIERZ_BUTTON).click()

    def z1_kliknij_element(self, index):
        self.find_all(self.Z1_ELEMENTY)[index].click()

    def z1_sprawdz_alert(self):
        assert self.find(self.Z1_ALERT).is_displayed()

    # Metody zadania 2:
    def z2_kliknij_wybierz_button(self):
        self.find(self.Z2_WYBIERZ_BUTTON).click()

    def z2_wyszukaj_tekst(self, element):
        self.find(self.Z2_WYSZUKAJ_INPUT).send_keys(element)

    def z2_kliknij_element(self, index):
        self.find_all(self.Z2_ELEMENTY)[index].click()

    def z2_sprawdz_alert(self):
        assert self.find(self.Z2_ALERT).is_displayed()
