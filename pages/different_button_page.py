from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import OrderDifferentButton

driver = webdriver.Firefox()

class DifferentButton:
    def __init__(self, driver):
        self.driver = driver

