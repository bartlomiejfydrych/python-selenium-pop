from locators.NiestandardoweListyLocators import NiestandardoweListyLocators


class NiestandardoweListyPage(NiestandardoweListyLocators):

    def __init__(self, driver):
        self.driver = driver

    # Metody zadania 1:
    def z1_kliknij_wybierz_button(self):
        self.driver.find_element(*self.Z1_WYBIERZ_BUTTON).click()

    def z1_kliknij_element(self, index):
        self.driver.find_elements(*self.Z1_ELEMENTY)[index].click()

    def z1_sprawdz_alert(self):
        assert self.driver.find_element(*self.Z1_ALERT).is_displayed()

    # Metody zadania 2:
    def z2_kliknij_wybierz_button(self):
        self.driver.find_element(*self.Z2_WYBIERZ_BUTTON).click()

    def z2_wyszukaj_tekst(self, element):
        self.driver.find_element(*self.Z2_WYSZUKAJ_INPUT).send_keys(element)

    def z2_kliknij_element(self, index):
        self.driver.find_elements(*self.Z2_ELEMENTY)[index].click()

    def z2_sprawdz_alert(self):
        assert self.driver.find_element(*self.Z2_ALERT).is_displayed()
