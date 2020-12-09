from locators.TabeleLocators import TabeleLocators
from log import log, for_all_methods
from pages.BasePage import BasePage


@for_all_methods(log)
class TabelePage(TabeleLocators, BasePage):
    wiek_janusza = None
    imie_warszawiaka = None
    srednia = 0.0
    sum = 0

    def odczytaj_dane_tabeli(self):
        for row in self.find_all(self.ROWS):
            cells = row.find_elements(*self.ROW_SELECTOR)
            imie = cells[0]
            wiek = cells[1]
            miasto = cells[2]
            TabelePage.sum += int(wiek.text)

            if imie.text == "Janusz":
                TabelePage.wiek_janusza = wiek.text
            if miasto.text == "Warszawa":
                TabelePage.imie_warszawiaka = imie.text

            TabelePage.srednia = float(TabelePage.sum) / float(len(self.find_all(self.ROWS)))

    def wpisz_srednia(self):
        self.find(self.SREDNIA_INPUT).send_keys(str(TabelePage.srednia))

    def wpisz_wiek(self):
        self.find(self.WIEK_INPUT).send_keys(TabelePage.wiek_janusza)

    def wpisz_imie(self):
        self.find(self.IMIE_INPUT).send_keys(TabelePage.imie_warszawiaka)

    def kliknij_sprawdz(self):
        self.find(self.SPRAWDZ_BUTTON).click()

    def sprawdz_alert(self):
        assert self.find(self.ALERT_MSG).is_displayed()
