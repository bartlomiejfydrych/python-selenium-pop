from locators.WiecejRamekLocators import WiecejRamekLocators


class WiecejRamekPage(WiecejRamekLocators):

    def __init__(self, driver):
        self.driver = driver

    # Metody formularza:
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

    # Metody ramek:
    def przejdz_do_domyslnego_okna(self):
        self.driver.switch_to.default_content()

    def przejdz_do_iframe2(self):
        self.driver.switch_to.frame(self.driver.find_element(*self.IFRAME2))

    def przejdz_do_iframe3(self):
        self.driver.switch_to.frame(self.driver.find_element(*self.IFRAME3))

    def przejdz_do_iframe4(self):
        self.driver.switch_to.frame(self.driver.find_element(*self.IFRAME4))

    def przejdz_do_iframe5(self):
        self.driver.switch_to.frame(self.driver.find_element(*self.IFRAME5))

    def przejdz_do_parent_frame(self):
        self.driver.switch_to.parent_frame()
