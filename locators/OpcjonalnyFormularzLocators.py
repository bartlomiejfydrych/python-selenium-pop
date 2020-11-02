from selenium.webdriver.common.by import By


class OpcjonalnyFormularzLocators:
    IMIE_INPUT = (By.ID, "firstName")
    NAZWISKO_INPUT = (By.ID, "lastName")
    EMAIL_INPUT = (By.ID, "email")
    MIASTO_INPUT = (By.ID, "city")
    ULICA_INPUT = (By.ID, "street")
    DODATKOWE_POLA_CHECKBOX = (By.CSS_SELECTOR, "label[for='add']")
    WYSLIJ_BUTTON = (By.ID, "submit")
    GRATULACJE_ALERT = (By.ID, "alert")
