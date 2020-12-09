from selenium.webdriver import ActionChains

from locators.PrzeciagnijUpuscLocators import PrzeciagnijUpuscLocators
from configurations import SCRIPT_PATH
from log import log, for_all_methods
from pages.BasePage import BasePage


@for_all_methods(log)
class PrzeciagnijUpuscPage(PrzeciagnijUpuscLocators, BasePage):

    # Metody zadania 1:------------------------------------------------------------------------------------------------
    def z1_przenies_elementy_do_grupy_b(self):
        for elements in self.find_all(self.Z1_ELEMENTY):
            self.actions.drag_and_drop(elements, self.find(self.Z1_GRUPA_B)).perform()

    def z1_sprawdz_alert_1(self):
        assert self.find(self.Z1_ALERT).is_displayed()

    # Metody zadania 2:------------------------------------------------------------------------------------------------
    def z2_posortuj_elementy(self):
        list_of_all_web_elements = []
        for data_order in range(5, 0, -1):
            list_of_all_web_elements.append(
                self.driver.find_element_by_css_selector(f"[data-order='{data_order}']"))

        for web_element in list_of_all_web_elements:
            smooth_move = ActionChains(self.driver).click_and_hold(web_element)
            for iterator in range(10):
                smooth_move.move_by_offset(0, -30)

            smooth_move.release().perform()

    def z2_sprawdz_alert_2(self):
        assert self.find(self.Z2_ALERT).is_displayed()

    # Metody zadania 3:------------------------------------------------------------------------------------------------
    def z3_przenies_elementy_do_grupy_y_html5(self):
        with open(SCRIPT_PATH) as f:
            full_script = f"{f.read()} \nsimulateHTML5DragAndDrop(arguments[0], arguments[1])"

        for element in self.find_all(self.Z3_ELEMENTY):
            self.driver.execute_script(full_script, element, self.find(self.Z3_GRUPA_Y))

    def z3_sprawdz_alert_3(self):
        assert self.find(self.Z3_ALERT).is_displayed()
