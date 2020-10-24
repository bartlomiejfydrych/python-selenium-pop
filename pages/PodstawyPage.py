from Locators import PodstawyLocators


class PodstawyPage(PodstawyLocators):

    def __init__(self, driver):
        self.driver = driver

    def wpisz_imie(self, imie):
        self.driver.find_element(*self.IMIE_INPUT).send_keys(imie)

    def wpisz_nazwisko(self, nazwisko):
        self.driver.find_element(*self.NAZWISKO_INPUT).send_keys(nazwisko)

    def wpisz_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def wpisz_miasto(self, miasto):
        self.driver.find_element(*self.MIASTO_INPUT).send_keys(miasto)

    def wpisz_ulica(self, ulica):
        self.driver.find_element(*self.ULICA_INPUT).send_keys(ulica)

    def akceptuj_regulamin(self):
        self.driver.find_element(*self.REGULAMIN_CHECKBOX).click()

    def wyslij_dane(self):
        self.driver.find_element(*self.WYSLIJ_BUTTON).click()

    def sprawdz_alert(self):
        assert self.driver.find_element(*self.GRATULACJE_ALERT).is_displayed()
