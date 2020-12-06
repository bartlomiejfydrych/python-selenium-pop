from locators.KomunikatyLocators import KomunikatyLocators
from pages.BasePage import BasePage
from log import log, for_all_methods


@for_all_methods(log)
class KomunikatyPage(KomunikatyLocators, BasePage):
    alert = None
    tekst = None

    def przejdz_na_alert(self):
        KomunikatyPage.alert = self.driver.switch_to.alert

    def pobierz_tekst_alert(self):
        KomunikatyPage.tekst = KomunikatyPage.alert.text

    def kliknij_wyswietl_komunikat(self):
        self.find(self.WYSWIETL_KOMUNIKAT_BUTTON).click()

    def kliknij_sprawdz_komunikat(self):
        self.find(self.SPRAWDZ_KOMUNIKAT_BUTTON).click()

    def wklej_komunikat(self):
        self.find(self.KOMUNIKAT_INPUT).send_keys(KomunikatyPage.tekst)

    def akceptuj_alert(self):
        KomunikatyPage.alert.accept()

    def odrzuc_alert(self):
        KomunikatyPage.alert.dismiss()

    def wyslij_tekst_do_alert(self, tekst):
        KomunikatyPage.alert.send_keys(tekst)

    def sprawdz_poprawnosc(self):
        assert self.find(self.GRATULACJE_ALERT).is_displayed()
