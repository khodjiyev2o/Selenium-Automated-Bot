import project.constants as const
from project.filtration import BookingFiltration
import os
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from prettytable import PrettyTable


class Booking(webdriver.Chrome):
    def __init__(self,driver_path=const.DRIVER_PATH,teardown=False):
        """options = webdriver.ChromeOptions()
        options.add_argument("start-maximized");
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")"""
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] +=  self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(15)
        self.big_div = self.find_big_div()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
            print('Exiting...')

    def land_first_page(self):
        self.get(const.BASE_URL)

    def search(self,where,check_in_date,check_out_date,guest_count):
        destination = self.find_element_by_css_selector('input[name="ss"]')
        destination.send_keys(where)
        destination_choice = self.find_element_by_css_selector('li[data-i="0"]')
        destination_choice.click()



        check_in = self.find_element_by_css_selector(
            f'td[data-date="{check_in_date}"]'
        )

        check_in.click()

        check_out = self.find_element_by_css_selector(
            f'td[data-date="{check_out_date}"]'
        )
        check_out.click()

        people_count = self.find_element_by_class_name('xp__guests__count')
        people_count.click()

        add_people_btn = self.find_element_by_xpath('//*[@id="xp__guests__inputs-container"]/div/div/div[1]/div/div[2]/button[2]')

        if guest_count != 1:
            for _ in range(guest_count-1):
                add_people_btn.click()
        else:
            pass

        search_btn = self.find_element_by_css_selector('button[data-sb-id="main"]')
        search_btn.click()

    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self)
        filtration.price_filter()

    def find_big_div(self):
        big_div = self.find_elements_by_css_selector('div[data-testid="property-card"]')
        return big_div

    def show_results(self):
        hotels_data = []
        for div in self.big_div:
            hotel_name = div.find_element_by_css_selector(
                'div[data-testid="title"]'
            ).get_attribute('innerHTML').strip()
            hotel_price = div.find_element_by_class_name(
                'b5cd09854e d10a6220b4'
            ).get_attribute('innerHTML').strip()
            hotel_score = div.find_element_by_class_name(
                'b5cd09854e d10a6220b4'
            ).get_attribute('innerHTML').strip()
            hotels_data.append([hotel_name,hotel_price,hotel_score])
        table = PrettyTable(
            field_names=["Hotel Name", "Hotel Price", "Hotel Score"]
        )
        table.add_rows(hotels_data)
        print(table)

    def change_language(self,language='en-us'):
        language_section = self.find_element_by_css_selector(
            'button[data-modal-id="language-selection"]'
        )
        language_section.click()

        language_button = self.find_element_by_css_selector(
            f'a[data-lang="{language}"]'
        )
        language_button.click()
