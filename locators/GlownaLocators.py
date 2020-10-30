from selenium.webdriver.common.by import By


class GlownaLocators:
    PODSTAWY_ZACZNIJ = (By.ID, "podstawy")
    WIECEJ_ELEMENTOW_ZACZNIJ = (By.ID, "wiecej")
    ASERCJA_ZACZNIJ = (By.ID, "asercja")
    LOKALIZATORY_ZACZNIJ = (By.CSS_SELECTOR, '[href="/testerczaki/lokalizatory"]')
    UKRYTE_ELEMENTY_ZACZNIJ = (By.CSS_SELECTOR, '[href="/testerczaki/ukryte"]')
    OPCJONALNY_FORMULARZ_ZACZNIJ = (By.CSS_SELECTOR, '[href="/testerczaki/opcjonalny"]')
    RAMKA_ZACZNIJ = (By.CSS_SELECTOR, '[href="/testerczaki/ramka"]')
    WIECEJ_RAMEK_ZACZNIJ = (By.CSS_SELECTOR, '[href="/testerczaki/ramki"]')
    OKNA_ZAKLADKI_ZACZNIJ = (By.CSS_SELECTOR, '[href="/testerczaki/okna"]')
    KOMUNIKATY_ZACZNIJ = (By.CSS_SELECTOR, '[href="/testerczaki/komunikaty"]')
    MENU_ZACZNIJ = (By.CSS_SELECTOR, '[href="/testerczaki/menu"]')
    PRZECIAGNIJ_UPUSC_ZACZNIJ = (By.CSS_SELECTOR, '[href="/testerczaki/przeciagnij"]')
    KLIKNIJ_PRZYTRZYMAJ_ZACZNIJ = (By.CSS_SELECTOR, '[href="/testerczaki/mysz"]')
    NIESTANDARDOWE_LISTY_ZACZNIJ = (By.CSS_SELECTOR, '[href="/testerczaki/listy"]')
    TABELE_ZACZNIJ = (By.CSS_SELECTOR, '[href="/testerczaki/tabele"]')
