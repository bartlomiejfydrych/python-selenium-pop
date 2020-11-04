from selenium.webdriver.common.by import By


class WiecejRamekLocators:
    #   Elementy formularza:
    IMIE_INPUT = (By.ID, "firstName")
    NAZWISKO_INPUT = (By.ID, "lastName")
    EMAIL_INPUT = (By.ID, "email")
    MIASTO_INPUT = (By.ID, "city")
    ULICA_INPUT = (By.ID, "street")
    REGULAMIN_CHECKBOX = (By.ID, "rules")
    WYSLIJ_BUTTON = (By.ID, "submit")
    GRATULACJE_ALERT = (By.ID, "alert")

    # Ramki:
    IFRAME2 = (By.CSS_SELECTOR, "[src='/testerczaki/iframe2.php']")
    IFRAME3 = (By.CSS_SELECTOR, "[src='/testerczaki/iframe3.php']")
    IFRAME4 = (By.CSS_SELECTOR, "[src='/testerczaki/iframe4.php']")
    IFRAME5 = (By.CSS_SELECTOR, "[src='/testerczaki/iframe5.php']")
