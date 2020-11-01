from tests.TestBase import TestBase


class UkryteElementyTest(TestBase):

    def test_ukryte_elementy(self):
        ukryte_elementy_page = self.glowna_page.go_to_ukryte_elementy_page()
        ukryte_elementy_page.wpisz_imie("Bartek")
        ukryte_elementy_page.wpisz_nazwisko("Bogucki")
        ukryte_elementy_page.wpisz_email("babo@interia.pl")
        ukryte_elementy_page.wpisz_miasto("Katowice")
        ukryte_elementy_page.wpisz_ulica("Mickiewicza 4a/12")
        ukryte_elementy_page.akceptuj_regulamin()
        ukryte_elementy_page.wyslij_dane()
        ukryte_elementy_page.sprawdz_alert()
