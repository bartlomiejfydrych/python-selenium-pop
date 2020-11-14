from selenium.webdriver.common.by import By


class NiestandardoweListyLocators:
    # Elementy zadania 1:
    Z1_WYBIERZ_BUTTON = (By.CSS_SELECTOR, "button:first-of-type")
    Z1_ELEMENTY = (By.CSS_SELECTOR, ".dropdown-menu > a")
    Z1_ALERT = (By.ID, "alert1")

    # Elementy zadania 2:
    Z2_WYBIERZ_BUTTON = (By.CSS_SELECTOR, "button#dropdown_coins")
    Z2_WYSZUKAJ_INPUT = (By.ID, "search2")
    Z2_ELEMENTY = (By.CSS_SELECTOR, "#menuItems > input")
    Z2_ALERT = (By.ID, "alert2")
