from selenium.webdriver import ActionChains

from locators.MenuLocators import MenuLocators


class MenuPage(MenuLocators):
    # TODO: Poprosić Dawida przy refactoringu by dokładnie to wszystko zbadał
    # Trzeba było to usunąć bo nazwaklasy.actions nie działało i trzeba było dać self.
    # actions = None

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)

    # Metody zadania 1:------------------------------------------------------------------------------------------------
    def z1_kliknij_link2(self):
        self.driver.find_element(*self.Z1_LINK2).click()

    def z1_sprawdz_alert(self):
        assert self.driver.find_element(*self.Z1_ALERT).is_displayed()

    # Metody zadania 2:------------------------------------------------------------------------------------------------
    def z2_rozwin_liste(self):
        self.driver.find_element(*self.Z2_ROZWIN_BUTTON).click()

    def z2_kliknij_link3(self):
        self.driver.find_element(*self.Z2_LINK3).click()

    def z2_sprawdz_alert(self):
        assert self.driver.find_element(*self.Z2_ALERT).is_displayed()

    # Metody zadania 3:------------------------------------------------------------------------------------------------
    def z3_kliknij_liste(self):
        self.driver.find_element(*self.Z3_LINK3).click()

    def z3_kliknij_link3_c(self):
        self.driver.find_element(*self.Z3_LINK3_C).click()

    def z3_sprawdz_alert(self):
        self.driver.find_element(*self.Z3_ALERT).is_displayed()

    # Metody zadania 4:------------------------------------------------------------------------------------------------
    def z4_kliknij_link3_b(self):
        self.actions.move_to_element(self.driver.find_element(*self.Z4_LINK3)) \
            .move_to_element(self.driver.find_element(*self.Z4_LINK3_B)).click().perform()

    def z4_sprawdz_alert(self):
        assert self.driver.find_element(*self.Z4_ALERT).is_displayed()

    # Metody zadania 5:------------------------------------------------------------------------------------------------
    def z5_kliknij_link3_b5(self):
        self.actions.move_to_element(self.driver.find_element(*self.Z5_LINK3)) \
            .move_to_element(self.driver.find_element(*self.Z5_LINK3_B)) \
            .move_to_element(self.driver.find_element(*self.Z5_LINK3_B1)) \
            .move_to_element(self.driver.find_element(*self.Z5_LINK3_B5)).click().perform()

    def z5_sprawdz_alert(self):
        assert self.driver.find_element(*self.Z5_ALERT).is_displayed()
