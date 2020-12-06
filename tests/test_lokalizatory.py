from tests.TestBase import TestBase


class TestLokalizatory(TestBase):

    def test_lokalizatory(self):
        lokalizatory_page = self.glowna_page.go_to_lokalizatory_page()
        lokalizatory_page.wpisz_imie("Bożena")
        lokalizatory_page.wpisz_nazwisko("Kołodziej")
        lokalizatory_page.wybierz_kraj("Meksyk")
        lokalizatory_page.wybierz_jezyk("Python", "JavaScript")
        lokalizatory_page.napisz_o_sobie("Studiuję prawo, jestem weganką i chciałabym, aby na świecie był pokój."
                                         "\n"
                                         "Zakręcona Netfliksiara nie bojąca się niczego oprócz wiecznej samotności.")
        lokalizatory_page.wyslij_plik()
        lokalizatory_page.wybierz_plec("Kobieta")
        lokalizatory_page.akceptuj_regilamin()
        lokalizatory_page.wyslij_dane()
        lokalizatory_page.sprawdz_alert()
