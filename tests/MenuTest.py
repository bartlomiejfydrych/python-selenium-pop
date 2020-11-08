from tests.TestBase import TestBase


class MenuTest(TestBase):
    menu_page = None

    def setUp(cls):
        super().setUp()
        cls.menu_page = cls.glowna_page.go_to_menu_page()

    def test_zadanie1(self):
        self.menu_page.z1_kliknij_link2()
        self.menu_page.z1_sprawdz_alert()

    def test_zadanie2(self):
        self.menu_page.z2_rozwin_liste()
        self.menu_page.z2_kliknij_link3()
        self.menu_page.z2_sprawdz_alert()

    def test_zadanie3(self):
        self.menu_page.z3_kliknij_liste()
        self.menu_page.z3_kliknij_link3_c()
        self.menu_page.z3_sprawdz_alert()

    def test_zadanie4(self):
        self.menu_page.z4_kliknij_link3_b()
        self.menu_page.z4_sprawdz_alert()

    def test_zadanie5(self):
        self.menu_page.z5_kliknij_link3_b5()
        self.menu_page.z5_sprawdz_alert()

    def test_wszystkie_zadania(self):
        self.menu_page.z1_kliknij_link2()
        self.menu_page.z1_sprawdz_alert()
        self.menu_page.z2_rozwin_liste()
        self.menu_page.z2_kliknij_link3()
        self.menu_page.z2_sprawdz_alert()
        self.menu_page.z3_kliknij_liste()
        self.menu_page.z3_kliknij_link3_c()
        self.menu_page.z3_sprawdz_alert()
        self.menu_page.z4_kliknij_link3_b()
        self.menu_page.z4_sprawdz_alert()
        self.menu_page.z5_kliknij_link3_b5()
        self.menu_page.z5_sprawdz_alert()
