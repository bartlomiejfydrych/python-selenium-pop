from tests.TestBase import TestBase


class TestPodstawy(TestBase):

    def test_podstawy(self):
        podstawy_page = self.glowna_page.go_to_podstawy_page()
        podstawy_page.wpisz_imie("Bartek")
        podstawy_page.wpisz_nazwisko("Bogucki")
        podstawy_page.wpisz_email("babo@interia.pl")
        podstawy_page.wpisz_miasto("Katowice")
        podstawy_page.wpisz_ulica("Mickiewicza 4a/12")
        podstawy_page.akceptuj_regulamin()
        podstawy_page.wyslij_dane()
        podstawy_page.sprawdz_alert()
