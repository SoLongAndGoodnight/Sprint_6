import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import OrderDifferentButton

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
    driver.find_element(*OrderDifferentButton.NAME).send_keys(name)

    # Заполняем фамилию
    driver.find_element(*OrderDifferentButton.LAST_NAME).send_keys(surname)

    # Заполняем адрес
    driver.find_element(*OrderDifferentButton.ADDRESS).send_keys(address)

    # Клик на поле с метро
    driver.find_element(*OrderDifferentButton.SUBWAY_FIELD).click()

    driver.find_element(*OrderDifferentButton.SUBWAY_SELECT).click()

    # Заполняем телефон

    driver.find_element(*OrderDifferentButton.PHONE).send_keys(phone)

    # Нажимаем кнопку "Далее"
    driver.find_element(*OrderDifferentButton.DALEE_BUTTON).click()

    # Заполняем календарь
    driver.find_element(*OrderDifferentButton.CALENDAR).click()

    driver.find_element(*OrderDifferentButton.CALENDAR_SELECT).click()

    # Указываем срок аренды
    driver.find_element(*OrderDifferentButton.RENT_DAYS).click()

    driver.find_element(*OrderDifferentButton.RENT_DAYS_SELECT).click()


    # Выбираем цвет
    driver.find_element(*OrderDifferentButton.COLOR).click()

    # Клик на кнопку "Заказать"
    driver.find_element(*OrderDifferentButton.ORDER_BUTTON).click()

    # Подтверждение заказа
    driver.find_element(*OrderDifferentButton.CONFIRM_BUTTON).click()

    # Ждем появления кнопки "Посмотреть статус"
    status_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[text()="Посмотреть статус"]'))
    )

    # Проверяем, что кнопка отображается
    assert status_button.is_displayed(), "Кнопка 'Посмотреть статус' не отображается на странице"
