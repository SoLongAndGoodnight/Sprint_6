import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

BASE_URL = "https://qa-scooter.praktikum-services.ru/"

def test_question_quantity(driver):
    driver.get(BASE_URL)
    driver.maximize_window()
    driver.implicitly_wait(3)

    # Скролл вниз на 500 пикселей
    for _ in range(4):
        driver.execute_script("window.scrollBy(0, 500);")
        driver.implicitly_wait(1)  # Небольшая пауза после скролла

    #ищем вопрос
    quantity = driver.find_element(By.XPATH, "//div[@id='accordion__heading-1' and @class='accordion__button']")

    #кликаем по вопросу
    quantity.click()

    expected_text = ("Пока что у нас так: один заказ — один самокат. "
                     "Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.")

    #ищем ожидаемый текст
    text_element = driver.find_element(By.XPATH,
                                       "//p[text()='Пока что у нас так: один заказ — один самокат. "
                                       "Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']")

    # Проверяем, что текст отобразился на странице
    assert expected_text in text_element.text, f"Текст не найден."
