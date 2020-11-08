from selenium.webdriver.common.by import By


class MenuLocators:
    # Elementy zadania 1:
    Z1_LINK2 = (By.CSS_SELECTOR, ".navbar-expand> .collapse > .navbar-nav > a:nth-child(2)")
    Z1_ALERT = (By.ID, "alert1")

    # Elementy zadania 2:
    Z2_ROZWIN_BUTTON = (By.CLASS_NAME, "m-2")
    Z2_LINK3 = (By.CSS_SELECTOR, "#navbarNavAltMarkup > .navbar-nav > a:nth-child(3)")
    Z2_ALERT = (By.ID, "alert2")

    # Elementy zadania 3:
    Z3_LINK3 = (By.CSS_SELECTOR, "[role='button']")
    Z3_LINK3_C = (By.CSS_SELECTOR, ".show > a:nth-child(3)")
    Z3_ALERT = (By.ID, "alert3")

    # Elementy zadania 4:
    Z4_LINK3 = (By.XPATH, "(//a[contains(@class,'dropdown-toggle')])[2]")
    Z4_LINK3_B = (By.XPATH, "(//div[contains(@class,'dropdown-menu')])[2]/a[2]")
    Z4_ALERT = (By.ID, "alert4")

    # Elementy zadania 5:
    Z5_LINK3 = (By.XPATH, "(//a[contains(@class,'dropdown-toggle')])[3]")
    Z5_LINK3_B = (By.CLASS_NAME, "hover2nd")
    Z5_LINK3_B1 = (By.CSS_SELECTOR, ".dropdown2nd > a:nth-child(1)")
    Z5_LINK3_B5 = (By.CSS_SELECTOR, ".dropdown2nd > a:nth-child(5)")
    Z5_ALERT = (By.ID, "alert5")
