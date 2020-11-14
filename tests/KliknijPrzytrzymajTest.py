from tests.TestBase import TestBase


class KliknijPrzytrzymajTest(TestBase):
    kliknij_przytrzymaj_page = None

    def setUp(cls):
        super().setUp()
        cls.kliknij_przytrzymaj_page = cls.glowna_page.go_to_kliknij_przytrzymaj_page()

    def test_zadanie1(self):
        self.kliknij_przytrzymaj_page.z1_kliknij_prawym()
        self.kliknij_przytrzymaj_page.z1_kliknij_opcje_2()
        self.kliknij_przytrzymaj_page.z1_sprawdz_alert()

    def test_zadanie2(self):
        self.kliknij_przytrzymaj_page.z2_przytrzymaj_przycisk()
        self.kliknij_przytrzymaj_page.z2_sprawdz_alert()

    def test_wszystkie_zadania(self):
        self.kliknij_przytrzymaj_page.z1_kliknij_prawym()
        self.kliknij_przytrzymaj_page.z1_kliknij_opcje_2()
        self.kliknij_przytrzymaj_page.z1_sprawdz_alert()
        self.kliknij_przytrzymaj_page.z2_przytrzymaj_przycisk()
        self.kliknij_przytrzymaj_page.z2_sprawdz_alert()
