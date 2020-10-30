from locators.WiecejElementowLocators import WiecejElementowLocators
from selenium.webdriver.support.ui import Select
from configurations import TESTFILE_PATH


class WiecejElementowPage(WiecejElementowLocators):

    def __init__(self, driver):
        self.driver = driver

    def wpisz_imie(self, imie):
        self.driver.find_element(*self.IMIE_INPUT).send_keys(imie)

    def wpisz_nazwisko(self, nazwisko):
        self.driver.find_element(*self.NAZWISKO_INPUT).send_keys(nazwisko)

    def wybierz_kraj(self, kraj_nazwa):
        select = Select(self.driver.find_element(*self.KRAJ_SELECT))
        select.select_by_visible_text(kraj_nazwa)

    def wybierz_jezyk(self, *jezyki):
        select = Select(self.driver.find_element(*self.JEZYK_SELECT))
        for jezyk_nazwa in jezyki:
            select.select_by_visible_text(jezyk_nazwa)

    def napisz_o_sobie(self, tekst):
        self.driver.find_element(*self.O_SOBIE_INPUT).send_keys(tekst)

    def wyslij_plik(self):
        self.driver.find_element(*self.PLIK_ZALACZNIK).send_keys(TESTFILE_PATH)

    def wybierz_plec(self, plec):
        if plec == "Mężczyzna":
            self.driver.find_element(*self.PLEC_MEZCZYZNA).click()
        elif plec == "Kobieta":
            self.driver.find_element(*self.PLEC_KOBIETA).click()
        elif plec == "Inne":
            self.driver.find_element(*self.PLEC_INNE).click()
        else:
            print("Źle podana płeć.")

    def akceptuj_regilamin(self):
        self.driver.find_element(*self.REGULAMIN_CHECKBOX).click()

    def wyslij_dane(self):
        self.driver.find_element(*self.WYSLIJ_BUTTON).click()

    def sprawdz_alert(self):
        assert self.driver.find_element(*self.GRATULACJE_ALERT).is_displayed()
