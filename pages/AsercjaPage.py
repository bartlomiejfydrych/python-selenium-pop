from locators.AsercjaLocators import AsercjaLocators
from log import log, for_all_methods

from pages.BasePage import BasePage


@for_all_methods(log)
class AsercjaPage(AsercjaLocators, BasePage):

    def wpisz_imie(self, imie):
        self.find(self.IMIE_INPUT).send_keys(imie)

    def wpisz_nazwisko(self, nazwisko):
        self.find(self.NAZWISKO_INPUT).send_keys(nazwisko)

    def wpisz_email(self, email):
        self.find(self.EMAIL_INPUT).send_keys(email)

    def wpisz_miasto(self, miasto):
        self.find(self.MIASTO_INPUT).send_keys(miasto)

    def wpisz_ulica(self, ulica):
        self.find(self.ULICA_INPUT).send_keys(ulica)

    def akceptuj_regulamin(self):
        self.find(self.REGULAMIN_CHECKBOX).click()

    def wyslij_dane(self):
        self.find(self.WYSLIJ_BUTTON).click()

    def sprawdz_alert(self):
        assert self.find(self.GRATULACJE_ALERT).is_displayed()

    def asercje_sprawdzajace_formularz(self, imie, nazwisko, email, miasto, ulica):
        oczekiwane_wartosci = [imie, nazwisko, email, miasto, ulica]
        selektory = [self.IMIE_INPUT, self.NAZWISKO_INPUT, self.EMAIL_INPUT, self.MIASTO_INPUT, self.ULICA_INPUT]
        for oczekiwana_wartosc, selektor in zip(oczekiwane_wartosci, selektory):
            actual = self.find(selektor).get_attribute("value")
            assert oczekiwana_wartosc == actual, f"'{oczekiwana_wartosc}' != '{actual}'"

    def asercja_sprawdzajaca_regulamin_checkbox(self):
        assert self.find(self.REGULAMIN_CHECKBOX).is_selected()


# ____________________________________________________________________________________________________________________
'''
DODATKOWE NOTATKI:

Zwykła, "pełna" metoda z asercjami sprawdzającymi formularz:

    def asercje_sprawdzajace_formularz(self, imie, nazwisko, email, miasto, ulica):
        self.tc.assertEqual(imie, self.driver.find_element(*self.IMIE_INPUT).get_attribute("value"))
        self.tc.assertEqual(nazwisko, self.driver.find_element(*self.NAZWISKO_INPUT).get_attribute("value"))
        self.tc.assertEqual(email, self.driver.find_element(*self.EMAIL_INPUT).get_attribute("value"))
        self.tc.assertEqual(miasto, self.driver.find_element(*self.MIASTO_INPUT).get_attribute("value"))
        self.tc.assertEqual(ulica, self.driver.find_element(*self.ULICA_INPUT).get_attribute("value"))

Inny sposób na asercję "Equals":

        assertEquals: assert imie == self.driver.find_element(*self.IMIE_INPUT).get_attribute("value")
        assertNotEquals: assert imie != self.driver.find_element(*self.IMIE_INPUT).get_attribute("value")
    LUB
        assert not imie == self.driver.find_element(*self.IMIE_INPUT).get_attribute("value")
'''
