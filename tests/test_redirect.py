import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import REDIRECT

BASE_URL = "https://qa-scooter.praktikum-services.ru/"

def test_redirect(driver):
    driver.get(BASE_URL)
    driver.implicitly_wait(3)

    driver.find_element(*REDIRECT.LOGO_REDIRECT).click()

    # Переключаемся на новую вкладку, если редирект открывает её
    driver.switch_to.window(driver.window_handles[-1])

    #ожидание редиректа
    WebDriverWait(driver, 5).until(
        EC.url_contains("dzen.ru"),
        message="Ожидание URL с 'dzen.ru' истекло"
    )

    # Проверяем, что редирект состоялся
    assert "dzen.ru" in driver.current_url, f"Редирект не состоялся, текущий URL: {driver.current_url}"