from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators.OpcjonalnyFormularzLocators import OpcjonalnyFormularzLocators


class OpcjonalnyFormularzPage(OpcjonalnyFormularzLocators):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def wpisz_imie(self, imie):
        self.driver.find_element(*self.IMIE_INPUT).send_keys(imie)

    def wpisz_nazwisko(self, nazwisko):
        self.driver.find_element(*self.NAZWISKO_INPUT).send_keys(nazwisko)

    def wpisz_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def dodatkowe_pola_kliknij(self):
        self.driver.find_element(*self.DODATKOWE_POLA_CHECKBOX).click()

    def wpisz_miasto(self, miasto):
        self.wait.until(ec.visibility_of_element_located(self.MIASTO_INPUT))
        self.driver.find_element(*self.MIASTO_INPUT).send_keys(miasto)

    def wpisz_ulica(self, ulica):
        self.wait.until(ec.visibility_of_element_located(self.ULICA_INPUT))
        self.driver.find_element(*self.ULICA_INPUT).send_keys(ulica)

    def wyslij_dane(self):
        self.driver.find_element(*self.WYSLIJ_BUTTON).click()

    def sprawdz_alert(self):
        assert self.driver.find_element(*self.GRATULACJE_ALERT).is_displayed()
