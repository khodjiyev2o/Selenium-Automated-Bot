import os
import pathlib
from selenium import webdriver
# Create your tests here.


os.environ['PATH'] += r'C:\Users\django\selenium'


def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()


