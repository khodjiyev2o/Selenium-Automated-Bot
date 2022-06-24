from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Results:
    def __init__(self,driver:WebDriver, hotels_container:WebElement,):
        self.driver = driver
        self.hotels_container = hotels_container
        self.hotel_list = self.hotel_list()
        self.driver.implicitly_wait(30)

    def hotel_list(self):
        hotel_list = self.hotels_container.find_elements_by_css_selector('div[data-testid="property-card"]')
        return hotel_list

    def show_results(self):
        hotels_data = []
        for div in self.hotel_list:

            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,'div[data-testid="title"]' ))
             )
            hotel_name = div.find_element_by_css_selector(
                'div[data-testid="title"]'
            ).get_attribute('innerHTML').strip()





            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "bd73d13072"))
            )
            price = div.find_element_by_class_name(
                'bd73d13072'
            ).get_attribute('innerHTML').strip()
            hotel_price =  price[9:] + price[0:3]




            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "bd73d13072"))
            )
            hotel_score = div.find_element_by_class_name(
                'd10a6220b4'
            ).get_attribute('innerHTML').strip()

            hotels_data.append([hotel_name, hotel_price, hotel_score])
        return hotels_data
