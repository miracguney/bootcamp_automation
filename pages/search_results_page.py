from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchResultsPage(BasePage):
    # Locator'lar
    SEARCH_RESULTS = (By.CSS_SELECTOR, "div.s-main-slot div.s-result-item")  # Arama sonuçları
    PAGE_2_LINK = (By.XPATH, "//a[contains(@href, 'page=2')]") # 2. sayfa bağlantısı
    CURRENT_PAGE = (By.CSS_SELECTOR, "span.s-pagination-selected")  # Şu anki sayfa numarası
    PRODUCT_LINK = (By.XPATH, "//div[contains(@class, 's-result-item') and @data-component-type='s-search-result']")# Ürün bağlantıları
    COOKIE_ACCEPT_BUTTON = (By.ID, "sp-cc-accept")# pop-up

    # Çerez pop-up'ın kapatılması
    def accept_cookies(self):
        try:
            cookie_button = self.driver.find_elements(*self.COOKIE_ACCEPT_BUTTON)# Çerez pop-up'ı kontrol ediliyor
            if cookie_button:
                cookie_button[0].click()# Çerez pop-up'ı kapatıldı.
        except Exception:
            pass

    # Arama sonuçlarının göründüğünü doğrulayan metot
    def verify_search_results(self, keyword):
        results = self.driver.find_elements(*self.SEARCH_RESULTS)
        assert len(results) > 0, f"'{keyword}' için arama sonucu bulunamadı!"

    # 2. sayfaya gitme ve doğrulama metodu
    def go_to_page_2(self):
        self.accept_cookies()
        self.click(self.PAGE_2_LINK)  # 2. sayfa bağlantısına tıkla
        current_page = self.find_element(self.CURRENT_PAGE).text
        assert current_page == "2", f"2. sayfada değiliz! Şu anki sayfa: {current_page}"

    # 3. ürüne tıklama metodu (0'dan başlayarak 2. indeks 3. ürün olur)
    def go_to_third_product(self):
        products = self.driver.find_elements(*self.PRODUCT_LINK)
        assert len(products) >= 3, "3. ürün bulunamadı!"
        products[2].click()  # 3. ürüne tıkla