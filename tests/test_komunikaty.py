from tests.TestBase import TestBase


class TestKomunikaty(TestBase):

    def test_komunikaty(self):
        komunikaty_page = self.glowna_page.go_to_komunikaty_page()
        komunikaty_page.kliknij_wyswietl_komunikat()
        komunikaty_page.przejdz_na_alert()
        komunikaty_page.pobierz_tekst_alert()
        komunikaty_page.akceptuj_alert()
        komunikaty_page.wklej_komunikat()
        komunikaty_page.kliknij_sprawdz_komunikat()
        komunikaty_page.akceptuj_alert()
        komunikaty_page.odrzuc_alert()
        komunikaty_page.wyslij_tekst_do_alert("tak")
        komunikaty_page.akceptuj_alert()
        komunikaty_page.sprawdz_poprawnosc()
