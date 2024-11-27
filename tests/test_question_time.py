import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

BASE_URL = "https://qa-scooter.praktikum-services.ru/"

def test_question_time(driver):
    driver.get(BASE_URL)
    driver.maximize_window()
    driver.implicitly_wait(3)

    # Скролл вниз на 500 пикселей
    for _ in range(4):
        driver.execute_script("window.scrollBy(0, 500);")
        driver.implicitly_wait(1)  # Небольшая пауза после скролла

    # ищем вопрос
    time = driver.find_element(By.XPATH, "//div[@id='accordion__heading-2' and @class='accordion__button']")

    #клик
    time.click()

    expected_text = ("Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. "
                     "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. "
                     "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.")

    # ищем ожидаемый текст
    text_element = driver.find_element(By.XPATH,
                                       "//p[text()='Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. "
                     "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. "
                     "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.']")

    assert expected_text in text_element.text, f"Текст не найден."