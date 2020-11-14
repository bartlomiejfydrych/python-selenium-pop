from selenium.webdriver import ActionChains

from locators.KliknijPrzytrzymajLocators import KliknijPrzytrzymajLocators


class KliknijPrzytrzymajPage(KliknijPrzytrzymajLocators):

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)

    # Metody zadania 1:
    def z1_kliknij_prawym(self):
        self.actions.context_click(self.driver.find_element(*self.Z1_PRAWY_PRZYCISK)).perform()

    def z1_kliknij_opcje_2(self):
        self.driver.find_element(*self.Z1_OPCJA2).click()

    def z1_sprawdz_alert(self):
        assert self.driver.find_element(*self.Z1_ALERT).is_displayed()

    # Metody zadania 2:
    # TODO: Zapytać Dawida o pauze na milisekundy
    def z2_przytrzymaj_przycisk(self):
        self.actions.click_and_hold(self.driver.find_element(*self.Z2_PRZYTRZYMAJ_PRZYCISK)).pause(
            4).release().perform()

    def z2_sprawdz_alert(self):
        assert self.driver.find_element(*self.Z2_ALERT).is_displayed()
