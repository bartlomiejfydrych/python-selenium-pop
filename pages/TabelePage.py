from locators.TabeleLocators import TabeleLocators


class TabelePage(TabeleLocators):
    wiek_janusza = None
    imie_warszawiaka = None
    srednia = 0.0
    sum = 0

    def __init__(self, driver):
        self.driver = driver

    def odczytaj_dane_tabeli(self):
        for row in self.driver.find_elements(*self.ROWS):
            cells = row.find_elements(*self.ROW_SELECTOR)
            imie = cells[0]
            wiek = cells[1]
            miasto = cells[2]
            TabelePage.sum += int(wiek.text)

            if imie.text == "Janusz":
                TabelePage.wiek_janusza = wiek.text
            if miasto.text == "Warszawa":
                TabelePage.imie_warszawiaka = imie.text

            TabelePage.srednia = float(TabelePage.sum) / float(len(self.driver.find_elements(*self.ROWS)))

    def wpisz_srednia(self):
        self.driver.find_element(*self.SREDNIA_INPUT).send_keys(str(TabelePage.srednia))

    def wpisz_wiek(self):
        self.driver.find_element(*self.WIEK_INPUT).send_keys(TabelePage.wiek_janusza)

    def wpisz_imie(self):
        self.driver.find_element(*self.IMIE_INPUT).send_keys(TabelePage.imie_warszawiaka)

    def kliknij_sprawdz(self):
        self.driver.find_element(*self.SPRAWDZ_BUTTON).click()

    def sprawdz_alert(self):
        assert self.driver.find_element(*self.ALERT_MSG).is_displayed()
