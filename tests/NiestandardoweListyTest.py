from tests.TestBase import TestBase


class NiestandardoweListyTest(TestBase):
    niestandardowe_listy_page = None

    def setUp(cls):
        super().setUp()
        cls.niestandardowe_listy_page = cls.glowna_page.go_to_niestandardowe_listy_page()

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
        self.niestandardowe_listy_page.z1_kliknij_wybierz_button()
        self.niestandardowe_listy_page.z1_kliknij_element(2)
        self.niestandardowe_listy_page.z1_sprawdz_alert()
        self.niestandardowe_listy_page.z2_kliknij_wybierz_button()
        self.niestandardowe_listy_page.z2_wyszukaj_tekst("Element")
        self.niestandardowe_listy_page.z2_kliknij_element(1)
        self.niestandardowe_listy_page.z2_sprawdz_alert()
