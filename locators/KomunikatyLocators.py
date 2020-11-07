from selenium.webdriver.common.by import By


class KomunikatyLocators:
    KOMUNIKAT_INPUT = (By.ID, "msg")
    WYSWIETL_KOMUNIKAT_BUTTON = (By.ID, "msgBtn")
    SPRAWDZ_KOMUNIKAT_BUTTON = (By.ID, "submit")
    GRATULACJE_ALERT = (By.ID, "alert")
