import time
import unittest
from selenium import webdriver
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

class AmazonTest(unittest.TestCase):
    def setUp(self):
        # Test başlamadan önce tarayıcıyı başlat
        self.driver = webdriver.Chrome()  # Chrome tarayıcısını başlat
        self.driver.maximize_window()  # Tarayıcıyı tam ekran yap

        # Sayfaları başlat
        self.home_page = HomePage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_page = CartPage(self.driver)

    def test_amazon_search_and_cart(self):
        # Adım 1: Amazon ana sayfasına git
        self.home_page.open()
        print("\n1) ana sayfa gidildi")

        # Adım 2: Ana sayfada olduğumuzu doğrula
        self.home_page.verify_home_page()
        print("2) ana sayfa doğrulandı")

        # Adım 3: Arama çubuğuna "samsung" yaz ve ara
        self.home_page.search("samsung")
        print("3) samsung yazılıp arandı")

        # Adım 4: Arama sonuçlarının göründüğünü doğrula
        self.search_results_page.verify_search_results("samsung")
        print("4) arama sonuçları göründü")

        # Adım 5: 2. sayfaya git ve 2. sayfada olduğumuzu doğrula
        self.search_results_page.go_to_page_2()
        print("5) 2. sayfaya gidildi ve doğrulandı")

        # Adım 6: 3. ürüne git
        self.search_results_page.go_to_third_product()
        print("6) 3. ürüne gidildi")

        # Adım 7: Ürün sayfasında olduğumuzu doğrula
        self.product_page.verify_product_page()
        print("7) ürün sayfasında olduğumuz doğrulandı")

        # Adım 8: Ürünü sepete ekle
        self.product_page.add_to_cart()
        print("8) ürün sepete eklendi")

        # Adım 9: Ürünün sepete eklendiğini doğrula  Bu zaten add_to_cart metodunda yapıldı, tekrar kontrol etmeye gerek yok
        print("9) Ürünün sepete eklendiğini doğrulandı")

        # Adım 10: Sepet sayfasına git
        self.cart_page.go_to_cart()
        print("10) sepet sayfasına gidildi")

        # Adım 11: Sepet sayfasında olduğumuzu ve ürünün eklendiğini doğrula
        self.cart_page.verify_cart_page()
        print("11) sepet sayfasında olduğumuz doğrulandı")

        # Adım 12: Ürünü sepetten sil ve sepetin boş olduğunu doğrula
        self.cart_page.delete_product()
        print("12) ürün sepetten silindi ve sepetin boş olduğu doğrulandı")

        # Adım 13: Ana sayfaya dön ve ana sayfada olduğumuzu doğrula
        self.home_page.open()
        self.home_page.verify_home_page()
        print("13) Ana sayfaya dönüldü ve anasayfada olduğumuz doğrulandı")

    def tearDown(self):
        # Test bittikten sonra tarayıcıyı kapat
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()