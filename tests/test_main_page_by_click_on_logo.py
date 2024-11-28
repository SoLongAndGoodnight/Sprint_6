import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import MainPageLogoClick


BASE_URL = "https://qa-scooter.praktikum-services.ru/order"

def test_main_page_by_click_on_logo(driver):
    driver.get(BASE_URL)
    driver.implicitly_wait(3)

    # ищем лого и кликаем
    #driver.find_element(By.XPATH, "//*[@class='Header_Logo__23yGT']").click()
    driver.find_element(*MainPageLogoClick.LOGO).click()

    #ищем на главной странице модуль и провеляем его отображение
    #logo = driver.find_element(By.XPATH, "//*[@class='Home_Header__iJKdX']")
    logo = driver.find_element(*MainPageLogoClick.LOGO)
    assert logo.is_displayed()
