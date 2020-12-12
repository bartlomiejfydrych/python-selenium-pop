from tests.TestBase import TestBase


class TestWiecejRamek(TestBase):

    def test_wiecej_ramek(self):
        wiecej_ramek_page = self.glowna_page.go_to_wiecej_ramek_page()
        wiecej_ramek_page.przejdz_do_iframe2()
        wiecej_ramek_page.wpisz_imie("Monika")
        wiecej_ramek_page.wpisz_nazwisko("Koparska")
        wiecej_ramek_page.przejdz_do_iframe3()
        wiecej_ramek_page.wpisz_email("monia69@amorki.pl")
        wiecej_ramek_page.przejdz_do_parent_frame()
        wiecej_ramek_page.przejdz_do_iframe4()
        wiecej_ramek_page.wpisz_miasto("Toruń")
        wiecej_ramek_page.przejdz_do_domyslnego_okna()
        wiecej_ramek_page.przejdz_do_iframe5()
        wiecej_ramek_page.wpisz_ulica("Misiewicza 12c/5")
        wiecej_ramek_page.przejdz_do_domyslnego_okna()
        wiecej_ramek_page.akceptuj_regulamin()
        wiecej_ramek_page.wyslij_dane()
        wiecej_ramek_page.sprawdz_alert()
        wiecej_ramek_page.przejdz_do_domyslnego_okna()
