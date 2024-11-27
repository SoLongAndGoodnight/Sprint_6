import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

BASE_URL = "https://qa-scooter.praktikum-services.ru/"

def test_question_cancellation(driver):
    driver.get(BASE_URL)
    driver.maximize_window()
    driver.implicitly_wait(3)

    # Скролл вниз на 700 пикселей
    for _ in range(4):
        driver.execute_script("window.scrollBy(0, 700);")
        driver.implicitly_wait(1)  # Небольшая пауза после скролла
    time.sleep(3)

    #поиск вопроса
    question_cancell = driver.find_element(By.XPATH, "//div[@id='accordion__heading-6' and @class='accordion__button']")

    #клик
    question_cancell.click()

    expected_text = ("Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.")

    # ищем ожидаемый текст
    text_element = driver.find_element(By.XPATH,
                                       "//p[text()='Да, пока самокат не привезли. "
                                       "Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']")

    assert expected_text in text_element.text, f"Текст не найден."