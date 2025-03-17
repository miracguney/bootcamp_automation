from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    # Locator'lar
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")  # Sepete ekle butonu
    CART_COUNT = (By.ID, "nav-cart-count")  # Sepet sayacı

    # Ürün sayfasında olduğumuzu doğrulayan metot
    def verify_product_page(self):
        current_url = self.get_current_url()
        assert "/dp/" in current_url, "Ürün sayfasında değiliz! URL: " + current_url

    # Ürünü sepete ekleme ve doğrulama metodu
    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)  # Sepete ekle butonuna tıkla
        cart_count = self.find_element(self.CART_COUNT).text
        assert int(cart_count) > 0, "Ürün sepete eklenmedi!"