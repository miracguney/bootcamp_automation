from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    # Locator'lar
    CART_LINK = (By.ID, "nav-cart")  # Sepet bağlantısı
    CART_ITEMS = (By.CSS_SELECTOR, "div.sc-list-item")  # Sepet öğeleri
    DELETE_BUTTON = (By.CSS_SELECTOR, "input[value='Sil']")  # Sil butonu
    CART_EMPTY_MESSAGE = (By.ID, "sc-subtotal-label-activecart") # Sepet boş mesajı

    # Sepete gitme metodu
    def go_to_cart(self):
        self.click(self.CART_LINK)

    # Sepet sayfasında olduğumuzu ve ürünün eklendiğini doğrulayan metot
    def verify_cart_page(self):
        current_url = self.get_current_url()
        assert "cart" in current_url, "Sepet sayfasında değiliz! URL: " + current_url
        items = self.driver.find_elements(*self.CART_ITEMS)
        assert len(items) > 0, "Sepette ürün yok!"

    # Ürünü sepetten silme ve doğrulama metodu
    def delete_product(self):
        self.click(self.DELETE_BUTTON)  # Sil butonuna tıkla
        empty_message = self.find_element(self.CART_EMPTY_MESSAGE).text
        assert "0 ürün" in empty_message.lower(), "Sepet boş değil!"  # "Ara Toplam (0 ürün)" kontrolü
        return empty_message