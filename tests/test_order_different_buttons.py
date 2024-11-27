import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://qa-scooter.praktikum-services.ru/"

@pytest.mark.parametrize("name, surname, address, phone, button_selector, scroll_needed", [
    ("Лизочка", "Тестова", "Примерная ул", "+7999004128", ".Button_Button__ra12g", False),  # Верхняя кнопка
    ("Андрей", "Иванов", "Тестовая ул, д. 5", "+7999123456", ".Button_Middle__1CSJM", True)  # Нижняя кнопка
])
def test_order(driver, name, surname, address, phone, button_selector, scroll_needed):
    driver.get(BASE_URL)
    driver.maximize_window()
    driver.implicitly_wait(3)

    # Скроллим вниз, если требуется
    if scroll_needed:
        driver.execute_script("window.scrollBy(0, 2000);")  # Скролл вниз на 400 пикселей
        time.sleep(4)  # Небольшая пауза для стабильности теста

    # Ищем кнопку "Заказать" и кликаем
    driver.find_element(By.CSS_SELECTOR, button_selector).click()

    # Заполняем модальник заказа
    # Заполняем имя
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='* Имя']").send_keys(name)

    # Заполняем фамилию
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='* Фамилия']").send_keys(surname)

    # Заполняем адрес
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']").send_keys(address)

    # Клик на поле с метро
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='* Станция метро']").click()
    driver.find_element(By.CSS_SELECTOR, ".select-search__options [data-index='1']").click()

    # Заполняем телефон
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']").send_keys(phone)

    # Нажимаем кнопку "Далее"
    driver.find_element(By.XPATH, "//button[contains(text(), 'Далее')]").click()

    # Заполняем календарь
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']").click()
    driver.find_element(By.XPATH, "//div[@aria-label='Choose воскресенье, 1-е декабря 2024 г.']").click()

    # Указываем срок аренды
    driver.find_element(By.XPATH, "//div[text()='* Срок аренды']").click()
    driver.find_element(By.XPATH, "//div[text()='трое суток']").click()

    # Выбираем цвет
    driver.find_element(By.ID, "black").click()

    # Клик на кнопку "Заказать"
    driver.find_element(By.XPATH, "//div[3]/button[2][text()='Заказать']").click()

    # Подтверждение заказа
    driver.find_element(By.XPATH, "//div[2]/button[2][text()='Да']").click()

    # Ждем появления кнопки "Посмотреть статус"
    status_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[text()="Посмотреть статус"]'))
    )

    # Проверяем, что кнопка отображается
    assert status_button.is_displayed(), "Кнопка 'Посмотреть статус' не отображается на странице"
