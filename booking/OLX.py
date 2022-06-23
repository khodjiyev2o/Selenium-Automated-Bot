import os
import pathlib
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create your tests here.


os.environ['PATH'] += r'C:\Users\django\selenium'
driver = webdriver.Chrome()


def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver.implicitly_wait(8)


def login():
    driver.get("https://smart.wsu.ac.kr/login.php")
    username = driver.find_element_by_xpath('//*[@id="input-username"]')
    password = driver.find_element_by_xpath('//*[@id="input-password"]')

    username.send_keys('202112120')
    password.send_keys('Samandar2021!')
    btn = driver.find_element_by_css_selector('input[name="loginbutton"]')
    #btn = driver.find_element_by_xpath('//*[@id="region-main"]/div/div/div/div[1]/div[1]/div[2]/form/div[2]/input')
    btn.click()


def logout():
    WebDriverWait(driver, 30).until(
        EC.url_to_be('http://smart.wsu.ac.kr/')
    )
    profile_btn = driver.find_element_by_xpath('//*[@id="page-header"]/nav/div/div[2]/ul/li[2]/a/img')
    profile_btn.click()
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="popover783192"]/div[2]/ul[1]/li[2]/a'))
    )

    logout_btn = driver.find_element_by_xpath('//*[@id="popover783192"]/div[2]/ul[1]/li[2]/a')

    try:
        logout_btn.click()
    except WebDriverException:
        print("Element is not clickable")



login()

