from selenium.webdriver.common.by import By


class UkryteElementyLocators:
    POPRAWNY_KONTENER = ".container>.row:nth-of-type(3) form "
    IMIE_INPUT = (By.CSS_SELECTOR, POPRAWNY_KONTENER + "#firstName")
    NAZWISKO_INPUT = (By.CSS_SELECTOR, POPRAWNY_KONTENER + "#lastName")
    EMAIL_INPUT = (By.CSS_SELECTOR, POPRAWNY_KONTENER + "#email")
    MIASTO_INPUT = (By.CSS_SELECTOR, POPRAWNY_KONTENER + "#city")
    ULICA_INPUT = (By.CSS_SELECTOR, POPRAWNY_KONTENER + "#street")
    REGULAMIN_CHECKBOX = (By.CSS_SELECTOR, POPRAWNY_KONTENER + "#rules")
    WYSLIJ_BUTTON = (By.CSS_SELECTOR, POPRAWNY_KONTENER + "#submit")
    GRATULACJE_ALERT = (By.CSS_SELECTOR, POPRAWNY_KONTENER + "#alert")
