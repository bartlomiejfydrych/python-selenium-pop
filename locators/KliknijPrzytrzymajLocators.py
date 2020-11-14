from selenium.webdriver.common.by import By


class KliknijPrzytrzymajLocators:

    # Elementy zadania 1:
    Z1_PRAWY_PRZYCISK = (By.ID, "contextClick")
    Z1_OPCJA2 = (By.CSS_SELECTOR, ".list-group > li:nth-child(2)")
    Z1_ALERT = (By.ID, "alert1")

    # Elementy zadania 2:
    Z2_PRZYTRZYMAJ_PRZYCISK = (By.ID, "holdClick")
    Z2_ALERT = (By.ID, "alert2")
