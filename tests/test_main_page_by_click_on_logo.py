import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


BASE_URL = "https://qa-scooter.praktikum-services.ru/order"

def test_main_page_by_click_on_logo(driver):
    driver.get(BASE_URL)
    driver.implicitly_wait(3)

    # ищем лого и кликаем
    driver.find_element(By.XPATH, "//*[@class='Header_Logo__23yGT']").click()

    #ищем на главной странице модуль и провеляем его отображение
    logo = driver.find_element(By.XPATH, "//*[@class='Home_Header__iJKdX']")
    assert logo.is_displayed()

