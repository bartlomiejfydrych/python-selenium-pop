from locators.AsercjaLocators import AsercjaLocators
import unittest


class AsercjaPage(AsercjaLocators):

    def __init__(self, driver):
        self.tc = unittest.TestCase()
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

    # TODO: Przypomnieć Dawidowi, że mieliśmy rozmawiać o tym gdzie umieszczać asercje. Czy w page czy w teście.
    def asercje_sprawdzajace_formularz(self, imie, nazwisko, email, miasto, ulica):
        zmienne = [imie, nazwisko, email, miasto, ulica]
        web_elementy = [self.IMIE_INPUT, self.NAZWISKO_INPUT, self.EMAIL_INPUT, self.MIASTO_INPUT, self.ULICA_INPUT]
        for zmienne_argumenty, elementy in zip(zmienne, web_elementy):
            self.tc.assertEqual(zmienne_argumenty, self.driver.find_element(*elementy).get_attribute("value"))

    def asercja_sprawdzajaca_regulamin_checkbox(self):
        assert self.driver.find_element(*self.REGULAMIN_CHECKBOX).is_selected()


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
