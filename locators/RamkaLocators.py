from selenium.webdriver.common.by import By


class RamkaLocators:
    IFRAME = (By.ID, "frame")
    IMIE_INPUT = (By.ID, "firstName")
    NAZWISKO_INPUT = (By.ID, "lastName")
    EMAIL_INPUT = (By.ID, "email")
    MIASTO_INPUT = (By.ID, "city")
    ULICA_INPUT = (By.ID, "street")
    REGULAMIN_CHECKBOX = (By.ID, "rules")
    WYSLIJ_BUTTON = (By.ID, "submit")
    GRATULACJE_ALERT = (By.ID, "alert")
