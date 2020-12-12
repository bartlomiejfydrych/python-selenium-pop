from tests.TestBase import TestBase


class TestWiecejElementow(TestBase):

    def test_wiecej_elementow(self):
        wiecej_elementow_page = self.glowna_page.go_to_wiecej_elementow_page()
        wiecej_elementow_page.wpisz_imie("Kondrad")
        wiecej_elementow_page.wpisz_nazwisko("Valenrod")
        wiecej_elementow_page.wybierz_kraj("Rosja")
        wiecej_elementow_page.wybierz_jezyk("Java", "C#")
        wiecej_elementow_page.napisz_o_sobie("Kocham małe zwierzątka i uwielbiam długie spacery po plaży. Mój tata"
                                             "to fanatyk wędkarstwa, całe mieszkanie wędkami zawalone."
                                             "\n"
                                             "Od rana do wieczora siedzi na forum Polskiego Związku Wędkarskiego i"
                                             " kłóci się z innymi Januszami.")
        wiecej_elementow_page.wyslij_plik()
        wiecej_elementow_page.wybierz_plec("Mężczyzna")
        wiecej_elementow_page.akceptuj_regilamin()
        wiecej_elementow_page.wyslij_dane()
        wiecej_elementow_page.sprawdz_alert()
