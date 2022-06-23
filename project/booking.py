import project.constants as const
import os
from selenium import webdriver


class Booking(webdriver.Chrome):
    def __init__(self,driver_path=const.DRIVER_PATH,teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] +=  self.driver_path
        super(Booking, self).__init__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
            print('Exiting...')

    def land_first_page(self):
        self.get(const.BASE_URL)
