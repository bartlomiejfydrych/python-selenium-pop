from tests.TestBase import TestBase


class TestOpcjonalnyFormularz(TestBase):

    def test_opcjonalny_formularz(self):
        opcjonalny_formularz_page = self.glowna_page.go_to_opcjonalny_formularz_page()
        opcjonalny_formularz_page.wpisz_imie("Marcin")
        opcjonalny_formularz_page.wpisz_nazwisko("Kapeć")
        opcjonalny_formularz_page.wpisz_email("kapkap@wp.pl")
        opcjonalny_formularz_page.dodatkowe_pola_kliknij()
        opcjonalny_formularz_page.wpisz_miasto("Chorzów")
        opcjonalny_formularz_page.wpisz_ulica("Chrobrego 5b/24")
        opcjonalny_formularz_page.wyslij_dane()
        opcjonalny_formularz_page.sprawdz_alert()
