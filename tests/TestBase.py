from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.GlownaPage import GlownaPage


class TestBase:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.glowna_page = GlownaPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        if hasattr(cls, "driver"):
            cls.driver.quit()

    def setup_method(self):
        self.close_redundant_windows()
        self.glowna_page.go_to_glowna_page()

    def close_redundant_windows(self):
        # Close all windows except first one
        for window in self.driver.window_handles[1:]:
            self.driver.switch_to.window(window)
            self.driver.close()

        # Switch to first window
        self.driver.switch_to.window(self.driver.window_handles[0])

