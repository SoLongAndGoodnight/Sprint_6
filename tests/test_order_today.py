import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from locators import OrderToday

BASE_URL = "https://qa-scooter.praktikum-services.ru/"

def test_question_price(driver):
    driver.get(BASE_URL)
    driver.maximize_window()
    driver.implicitly_wait(3)

    # Скролл вниз на 500 пикселей
    for _ in range(4):
        driver.execute_script("window.scrollBy(0, 500);")
        driver.implicitly_wait(1)  # Небольшая пауза после скролла
    time.sleep(3)

    #поиск вопроса
    order_today = driver.find_element(*OrderToday.QUESTION)

    #клик
    order_today.click()

    expected_text = ("Только начиная с завтрашнего дня. Но скоро станем расторопнее.")

    #ищем ожидаемый текст
    text_element = driver.find_element(*OrderToday.ANSWER)

    assert expected_text in text_element.text, f"Текст не найден."

