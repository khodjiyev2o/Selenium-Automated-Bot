from selenium.webdriver.remote.webdriver import WebDriver


class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def price_filter(self):
        filter_price = self.driver.find_element_by_css_selector('a[data-type="price"]')
        filter_price.click()