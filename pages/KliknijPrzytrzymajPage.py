from locators.KliknijPrzytrzymajLocators import KliknijPrzytrzymajLocators
from log import log, for_all_methods
from pages.BasePage import BasePage


@for_all_methods(log)
class KliknijPrzytrzymajPage(KliknijPrzytrzymajLocators, BasePage):

    # Metody zadania 1:
    def z1_kliknij_prawym(self):
        self.actions.context_click(self.find(self.Z1_PRAWY_PRZYCISK)).perform()

    def z1_kliknij_opcje_2(self):
        self.find(self.Z1_OPCJA2).click()

    def z1_sprawdz_alert(self):
        assert self.find(self.Z1_ALERT).is_displayed()

    # Metody zadania 2:
    def z2_przytrzymaj_przycisk(self):
        przycisk = self.find(self.Z2_PRZYTRZYMAJ_PRZYCISK)
        self.actions.click_and_hold(przycisk).pause(3.5).release().perform()

    def z2_sprawdz_alert(self):
        assert self.find(self.Z2_ALERT).is_displayed()
