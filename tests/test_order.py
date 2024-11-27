import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://qa-scooter.praktikum-services.ru/"

@pytest.mark.parametrize("name, surname, address, phone", [
    ("Лизочка", "Тестова", "Примерная ул", "+7999004128"),
    ("Андрей", "Иванов", "Тестовая ул, д. 5", "+7999123456")])

def test_order(driver, name, surname, address, phone):
    driver.get(BASE_URL)
    driver.maximize_window()
    driver.implicitly_wait(3)
    #ищем кнопку "Заказать" и кликаем
    driver.find_element(By.CSS_SELECTOR, ".Button_Button__ra12g").click()

    #заполняем модальник заказа
    #заполняем имя
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='* Имя']").send_keys(name)

    #заполняем фамилию
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='* Фамилия']").send_keys(surname)

    #заполеяем адрес
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']").send_keys(address)

    #клик на поле с метро
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='* Станция метро']").click()
    driver.find_element(By.CSS_SELECTOR, ".select-search__options [data-index='1']").click()

    #заполняем телефон
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']").send_keys(phone)

    #нажимаем кнопку "далее"
    driver.find_element(By.XPATH, "//button[contains(text(), 'Далее')]").click()

    #заполняем календарь
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']").click()
    driver.find_element(By.XPATH, "//div[@aria-label='Choose воскресенье, 1-е декабря 2024 г.']").click()

    #указываем срок аренды
    driver.find_element(By.XPATH, "//div[text()='* Срок аренды']").click()
    driver.find_element(By.XPATH, "//div[text()='трое суток']").click()

    #выбираем цвет
    driver.find_element(By.ID, "black").click()

    #клик на кнопку "Заказать"
    driver.find_element(By.XPATH, "//div[3]/button[2][text()='Заказать']").click()
    #time.sleep(3)

    #подтверждение заказа
    driver.find_element(By.XPATH, "//div[2]/button[2][text()='Да']").click()

    #ждем появление кнопки "Посмотреть статус"
    status_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Посмотреть статус"]')))

    # Проверка, что элемент отображается
    assert status_button.is_displayed(), "Кнопка 'Посмотреть статус' не отображается на странице"






