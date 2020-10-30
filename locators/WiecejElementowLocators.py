from selenium.webdriver.common.by import By


class WiecejElementowLocators:
    IMIE_INPUT = (By.ID, "firstName")
    NAZWISKO_INPUT = (By.ID, "lastName")
    KRAJ_SELECT = (By.ID, "country")
    JEZYK_SELECT = (By.ID, "lang")
    O_SOBIE_INPUT = (By.ID, "about")
    PLIK_ZALACZNIK = (By.ID, "file")

    # Płeć:
    PLEC_MEZCZYZNA = (By.ID, "maleLabel")
    PLEC_KOBIETA = (By.ID, "femaleLabel")
    PLEC_INNE = (By.ID, "otherLabel")

    REGULAMIN_CHECKBOX = (By.ID, "rulesLabel")
    WYSLIJ_BUTTON = (By.ID, "submit")
    GRATULACJE_ALERT = (By.CLASS_NAME, "alert-success")