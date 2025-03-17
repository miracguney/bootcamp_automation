from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # 10 saniye bekleme süresi

    # elementi bulup görünür olmasını bekleyen metot
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    # tıklama yapan metot
    def click(self, locator):
        self.find_element(locator).click()

    # metin yazan metot
    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    # Sayfanın URL'sini döndüren metot
    def get_current_url(self):
        return self.driver.current_url