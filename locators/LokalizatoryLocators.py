from selenium.webdriver.common.by import By


class LokalizatoryLocators:
    IMIE_INPUT = (By.CLASS_NAME, "firstName")
    NAZWISKO_INPUT = (By.CSS_SELECTOR, "[placeholder='Nazwisko']")
    KRAJ_SELECT = (By.CLASS_NAME, "custom-select")
    JEZYK_SELECT = (By.CSS_SELECTOR, "[data-custom='lang']")
    O_SOBIE_INPUT = (By.CSS_SELECTOR, "[rows='4']")
    PLIK_ZALACZNIK = (By.CSS_SELECTOR, "[type='file']")

    # Płeć:
    PLEC_MEZCZYZNA = (By.CSS_SELECTOR, "div.mb-3>div.custom-radio:nth-of-type(1)>.custom-control-label")
    PLEC_KOBIETA = (By.CSS_SELECTOR, "div.mb-3>div.custom-radio:nth-of-type(2)>.custom-control-label")
    PLEC_INNE = (By.CSS_SELECTOR, "div.mb-3>div.custom-radio:nth-of-type(3)>.custom-control-label")

    REGULAMIN_CHECKBOX = (By.CSS_SELECTOR, "div.custom-checkbox>.custom-control-label")
    WYSLIJ_BUTTON = (By.CLASS_NAME, "btn-primary")
    GRATULACJE_ALERT = (By.CLASS_NAME, "alert-success")