import pytest
import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

from pages.main_page import MainPage
from pages.login_page import LoginPage


link = "http://selenium1py.pythonanywhere.com/"


def test_guest_go_to_login_page(browser: WebDriver):
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser: WebDriver):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
