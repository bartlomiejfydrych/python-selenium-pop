from tests.TestBase import TestBase


class TabeleTest(TestBase):

    def test_tabele(self):
        tabele_page = self.glowna_page.go_to_tabele_page()
        tabele_page.odczytaj_dane_tabeli()
        tabele_page.wpisz_srednia()
        tabele_page.wpisz_wiek()
        tabele_page.wpisz_imie()
        tabele_page.kliknij_sprawdz()
        tabele_page.sprawdz_alert()
