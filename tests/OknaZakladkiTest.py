from pages.PodstawyPage import PodstawyPage
from tests.TestBase import TestBase

# TODO: Zwrócić Dawidowi uwagę, że po pierwszym teście coś przeglądarka się nie zamyka i czy to tak ma być

class OknaZakladkiTest(TestBase):

    def wypelnij_podstawy_page(self):
        podstawy_page = PodstawyPage(self.driver)
        podstawy_page.wpisz_imie("Agata")
        podstawy_page.wpisz_nazwisko("Rogacka")
        podstawy_page.wpisz_email("agness@wp.pl")
        podstawy_page.wpisz_miasto("Płock")
        podstawy_page.wpisz_ulica("Kafarka 7c/17")
        podstawy_page.akceptuj_regulamin()
        podstawy_page.wyslij_dane()
        podstawy_page.sprawdz_alert()

    def test_poprawne_zalogowanie_karta(self):
        okna_zakladki_page = self.glowna_page.go_to_okna_zakladki_page()
        okna_zakladki_page.otworz_podstawy_nowa_karta()
        okna_zakladki_page.przelacz_karte_lub_okno(1)
        self.wypelnij_podstawy_page()

    def test_poprawne_zalogowanie_okno(self):
        okna_zakladki_page = self.glowna_page.go_to_okna_zakladki_page()
        okna_zakladki_page.otworz_podstawy_nowe_okno()
        okna_zakladki_page.przelacz_karte_lub_okno(1)
        okna_zakladki_page.powieksz_okno()
        self.wypelnij_podstawy_page()
