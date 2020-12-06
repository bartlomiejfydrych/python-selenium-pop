from tests.TestBase import TestBase


class TestAsercja(TestBase):
    imie = "Wiktor"
    nazwisko = "Frankenstein"
    email = "wiktorfrank@amorki.pl"
    miasto = "Kraków"
    ulica = "Maczety 3a/20"

    def test_asercja(self):
        asercja_page = self.glowna_page.go_to_asercja_page()
        asercja_page.wpisz_imie(self.imie)
        asercja_page.wpisz_nazwisko(self.nazwisko)
        asercja_page.wpisz_email(self.email)
        asercja_page.wpisz_miasto(self.miasto)
        asercja_page.wpisz_ulica(self.ulica)
        asercja_page.asercje_sprawdzajace_formularz(self.imie, self.nazwisko, self.email, self.miasto, self.ulica)
        asercja_page.akceptuj_regulamin()
        asercja_page.asercja_sprawdzajaca_regulamin_checkbox()
        asercja_page.wyslij_dane()
        asercja_page.sprawdz_alert()
