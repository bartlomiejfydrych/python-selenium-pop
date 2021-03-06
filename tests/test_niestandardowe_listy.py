from tests.TestBase import TestBase


class TestNiestandardoweListy(TestBase):
    niestandardowe_listy_page = None

    def setup_method(self):
        super().setup_method()
        self.niestandardowe_listy_page = self.glowna_page.go_to_niestandardowe_listy_page()

    def test_zadanie1(self):
        self.niestandardowe_listy_page.z1_kliknij_wybierz_button()
        self.niestandardowe_listy_page.z1_kliknij_element(2)
        self.niestandardowe_listy_page.z1_sprawdz_alert()

    def test_zadanie2(self):
        self.niestandardowe_listy_page.z2_kliknij_wybierz_button()
        self.niestandardowe_listy_page.z2_wyszukaj_tekst("Element")
        self.niestandardowe_listy_page.z2_kliknij_element(1)
        self.niestandardowe_listy_page.z2_sprawdz_alert()

    def test_wszystkie_zadania(self):
        self.test_zadanie1()
        self.test_zadanie2()
