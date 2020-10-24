import unittest
from pages.PodstawyPage import PodstawyPage
from tests.TestBase import TestBase


class PodstawyTest(TestBase):

    def test_podstawy(self):
        driver = self.driver

        self.driver.get("http://dawidkaruga.pl/testerczaki/podstawy")

        podstawy_page = PodstawyPage(driver)
        podstawy_page.wpisz_imie("Bartek")
        podstawy_page.wpisz_nazwisko("Bogucki")
        podstawy_page.wpisz_email("babo@interia.pl")
        podstawy_page.wpisz_miasto("Katowice")
        podstawy_page.wpisz_ulica("Mickiewicza 4a/12")
        podstawy_page.akceptuj_regulamin()
        podstawy_page.wyslij_dane()
        podstawy_page.sprawdz_alert()


if __name__ == '__main__':
    unittest.main()
