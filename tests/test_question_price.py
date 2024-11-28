import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from locators import QuestionPrice

BASE_URL = "https://qa-scooter.praktikum-services.ru/"

def test_question_price(driver):
    driver.get(BASE_URL)
    driver.maximize_window()
    driver.implicitly_wait(3)

    # Прокручиваем до вопроса
    for _ in range(4):
        driver.execute_script("window.scrollBy(0, 500);")  # Скролл вниз на 500 пикселей
        driver.implicitly_wait(1)  # Небольшая пауза после скролла
    time.sleep(3)
    price = driver.find_element(*QuestionPrice.QUESTION)

    # Кликаем на элемент
    price.click()

    # Ищем текст, который должен отобразиться после клика
    expected_text = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    text_element = driver.find_element(*QuestionPrice.ANSWER)

    # Проверяем, что текст отобразился на странице
    assert expected_text in text_element.text, f"Текст не найден."
