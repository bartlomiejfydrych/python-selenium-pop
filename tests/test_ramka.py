from tests.TestBase import TestBase


class TestRamka(TestBase):

    def test_ramka(self):
        ramka_page = self.glowna_page.go_to_ramka_page()
        ramka_page.przejdz_do_iframe()
        ramka_page.wpisz_imie("Robert")
        ramka_page.wpisz_nazwisko("Koczybowski")
        ramka_page.wpisz_email("fartman@o2.pl")
        ramka_page.wpisz_miasto("Gliwice")
        ramka_page.wpisz_ulica("Macierewicza 7g/42")
        ramka_page.akceptuj_regulamin()
        ramka_page.wyslij_dane()
        ramka_page.sprawdz_alert()
        ramka_page.przejdz_do_domyslnego_okna()
