from locators.MenuLocators import MenuLocators
from pages.BasePage import BasePage
from log import log, for_all_methods


@for_all_methods(log)
class MenuPage(MenuLocators, BasePage):

    # Metody zadania 1:------------------------------------------------------------------------------------------------
    def z1_kliknij_link2(self):
        self.find(self.Z1_LINK2).click()

    def z1_sprawdz_alert(self):
        assert self.find(self.Z1_ALERT).is_displayed()

    # Metody zadania 2:------------------------------------------------------------------------------------------------
    def z2_rozwin_liste(self):
        self.find(self.Z2_ROZWIN_BUTTON).click()

    def z2_kliknij_link3(self):
        self.find(self.Z2_LINK3).click()

    def z2_sprawdz_alert(self):
        assert self.find(self.Z2_ALERT).is_displayed()

    # Metody zadania 3:------------------------------------------------------------------------------------------------
    def z3_kliknij_liste(self):
        self.find(self.Z3_LINK3).click()

    def z3_kliknij_link3_c(self):
        self.find(self.Z3_LINK3_C).click()

    def z3_sprawdz_alert(self):
        self.find(self.Z3_ALERT).is_displayed()

    # Metody zadania 4:------------------------------------------------------------------------------------------------
    def z4_kliknij_link3_b(self):
        z4_link3 = self.find(self.Z4_LINK3)
        z4_link3_b = self.find(self.Z4_LINK3_B)
        self.actions.move_to_element(z4_link3) \
            .move_to_element(z4_link3_b) \
            .click().perform()

    def z4_sprawdz_alert(self):
        assert self.find(self.Z4_ALERT).is_displayed()

    # Metody zadania 5:------------------------------------------------------------------------------------------------
    def z5_kliknij_link3_b5(self):
        z5_link3 = self.find(self.Z5_LINK3)
        z5_link3_b = self.find(self.Z5_LINK3_B)
        z5_link3_b1 = self.find(self.Z5_LINK3_B1)
        z5_link3_b5 = self.find(self.Z5_LINK3_B5)
        self.actions.move_to_element(z5_link3) \
            .move_to_element(z5_link3_b) \
            .move_to_element(z5_link3_b1) \
            .move_to_element(z5_link3_b5) \
            .click().perform()

    def z5_sprawdz_alert(self):
        assert self.find(self.Z5_ALERT).is_displayed()
