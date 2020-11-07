from selenium.webdriver.common import alert

from locators.KomunikatyLocators import KomunikatyLocators


class KomunikatyPage(KomunikatyLocators):
    alert = None
    tekst = None

    def __init__(self, driver):
        self.driver = driver

    def przejdz_na_alert(self):
        KomunikatyPage.alert = self.driver.switch_to.alert

    def pobierz_tekst_alert(self):
        KomunikatyPage.tekst = KomunikatyPage.alert.text

    def kliknij_wyswietl_komunikat(self):
        self.driver.find_element(*self.WYSWIETL_KOMUNIKAT_BUTTON).click()

    def kliknij_sprawdz_komunikat(self):
        self.driver.find_element(*self.SPRAWDZ_KOMUNIKAT_BUTTON).click()

    def wklej_komunikat(self):
        self.driver.find_element(*self.KOMUNIKAT_INPUT).send_keys(KomunikatyPage.tekst)

    def akceptuj_alert(self):
        KomunikatyPage.alert.accept()

    def odrzuc_alert(self):
        KomunikatyPage.alert.dismiss()

    def wyslij_tekst_do_alert(self, tekst):
        KomunikatyPage.alert.send_keys(tekst)

    def sprawdz_poprawnosc(self):
        assert self.driver.find_element(*self.GRATULACJE_ALERT).is_displayed()
