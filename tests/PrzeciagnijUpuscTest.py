from tests.TestBase import TestBase


class PrzeciagnijUpuscTest(TestBase):
    przeciagnij_upusc_page = None

    def setUp(cls):
        super().setUp()
        cls.przeciagnij_upusc_page = cls.glowna_page.go_to_przeciagnij_upusc_page()

    def test_zadanie1(self):
        self.przeciagnij_upusc_page.z1_przenies_elementy_do_grupy_b()
        self.przeciagnij_upusc_page.z1_sprawdz_alert_1()

    def test_zadanie2(self):
        self.przeciagnij_upusc_page.z2_posortuj_elementy()
        self.przeciagnij_upusc_page.z2_sprawdz_alert_2()

    def test_zadanie3(self):
        self.przeciagnij_upusc_page.z3_przenies_elementy_do_grupy_y_html5()
        self.przeciagnij_upusc_page.z3_sprawdz_alert_3()

    def test_wszystkie_zadania(self):
        self.przeciagnij_upusc_page.z1_przenies_elementy_do_grupy_b()
        self.przeciagnij_upusc_page.z1_sprawdz_alert_1()
        self.przeciagnij_upusc_page.z2_posortuj_elementy()
        self.przeciagnij_upusc_page.z2_sprawdz_alert_2()
        self.przeciagnij_upusc_page.z3_przenies_elementy_do_grupy_y_html5()
        self.przeciagnij_upusc_page.z3_sprawdz_alert_3()
