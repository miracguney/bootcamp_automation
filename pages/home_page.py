from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    # Locator'lar
    SEARCH_BAR = (By.ID, "twotabsearchtextbox")  # Arama çubuğunun ID'si
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")  # Arama butonunun ID'si

    # Sayfayı açan metot
    def open(self):
        self.driver.get("https://www.amazon.com.tr/")

    # Ana sayfada olduğumuzu doğrulayan metot
    def verify_home_page(self):
        current_url = self.get_current_url()
        assert "amazon.com.tr" in current_url, "Ana sayfada değiliz! URL: " + current_url

    # Arama çubuğuna metin yazıp arama yapan metot
    def search(self, keyword):
        self.send_keys(self.SEARCH_BAR, keyword)  # Arama çubuğuna metni yaz
        self.click(self.SEARCH_BUTTON)  # Arama butonuna tıkla