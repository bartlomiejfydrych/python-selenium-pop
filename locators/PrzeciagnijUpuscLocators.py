from selenium.webdriver.common.by import By


class PrzeciagnijUpuscLocators:

    # Elementy zadania 1:
    Z1_GRUPA_B = (By.ID, "simpleList2")
    Z1_ALERT = (By.ID, "alert1")
    Z1_ELEMENTY = (By.CSS_SELECTOR, "#simpleList1 li")

    # Elementy zadania 2:
    Z2_ALERT = (By.ID, "alert2")

    # Elementy zadania 3:
    Z3_ELEMENTY = (By.CSS_SELECTOR, "#simpleList4 > li")
    Z3_ELEMENT_1X = (By.ID, "test1")
    Z3_ELEMENT_2X = (By.ID, "test2")
    Z3_GRUPA_Y = (By.ID, "simpleList5")
    Z3_ALERT = (By.ID, "alert3")
