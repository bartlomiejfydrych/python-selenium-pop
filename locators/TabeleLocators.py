from selenium.webdriver.common.by import By


class TabeleLocators:

    SREDNIA_INPUT = (By.ID, "avg")
    WIEK_INPUT = (By.ID, "age")
    IMIE_INPUT = (By.ID, "name")
    SPRAWDZ_BUTTON = (By.ID, "submit1")
    ALERT_MSG = (By.ID, "alert1")
    ROWS = (By.CSS_SELECTOR, "#table1 tr")
    ROW_SELECTOR = (By.CSS_SELECTOR, "td")
