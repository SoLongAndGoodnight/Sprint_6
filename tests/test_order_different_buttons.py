import time

import pytest
from pages.order_page import OrderPageObject

BASE_URL = "https://qa-scooter.praktikum-services.ru/"


@pytest.mark.parametrize("name, surname, address, phone, is_upper_button, scroll_needed", [
    ("Лизочка", "Тестова", "Примерная ул", "+7999004128", True, False),  # Верхняя кнопка
    ("Андрей", "Иванов", "Тестовая ул, д. 5", "+7999123456", False, True)  # Нижняя кнопка
])
def test_order(driver, name, surname, address, phone, is_upper_button, scroll_needed):
    driver.get(BASE_URL)
    driver.maximize_window()
    driver.implicitly_wait(3)

    page_object = OrderPageObject(driver)

    # Скроллим вниз, если требуется
    if scroll_needed:
        driver.execute_script("window.scrollBy(0, 2000);")  # Скролл вниз на 400 пикселей
        time.sleep(4)  # Небольшая пауза для стабильности теста

    # Ищем кнопку "Заказать" и кликаем
    if is_upper_button:
        page_object.upper_order_button_click()
    else:
        page_object.bottom_order_button_click()
    # driver.find_element(By.CSS_SELECTOR, button_selector).click()

    # Заполняем модальник заказа
    # Заполняем имя
    # driver.find_element(*OrderDifferentButton.NAME).send_keys(name)
    page_object.name_fill(name)

    # Заполняем фамилию
    #driver.find_element(*OrderDifferentButton.LAST_NAME).send_keys(surname)
    page_object.surname_fill(surname)

    # Заполняем адрес
    #driver.find_element(*OrderDifferentButton.ADDRESS).send_keys(address)
    page_object.address_fill(address)

    # Клик на поле с метро
    #driver.find_element(*OrderDifferentButton.SUBWAY_FIELD).click()
    page_object.subway_dropdown_click()

    #driver.find_element(*OrderDifferentButton.SUBWAY_SELECT).click()
    page_object.subway_select()

    # Заполняем телефон
    #driver.find_element(*OrderDifferentButton.PHONE).send_keys(phone)
    page_object.phone_fill(phone)

    # Нажимаем кнопку "Далее"
    #driver.find_element(*OrderDifferentButton.DALEE_BUTTON).click()
    page_object.dalee_button()

    # Заполняем календарь
    #driver.find_element(*OrderDifferentButton.CALENDAR).click()
    page_object.calendar_click()

    #driver.find_element(*OrderDifferentButton.CALENDAR_SELECT).click()
    page_object.calendar_select()

    # Указываем срок аренды
    #driver.find_element(*OrderDifferentButton.RENT_DAYS).click()
    page_object.rent_click()

    #driver.find_element(*OrderDifferentButton.RENT_DAYS_SELECT).click()
    page_object.rent_select()

    # Выбираем цвет
    #driver.find_element(*OrderDifferentButton.COLOR).click()
    page_object.color_click()

    # Клик на кнопку "Заказать"
    #driver.find_element(*OrderDifferentButton.ORDER_BUTTON).click()
    page_object.order_button()

    # Подтверждение заказа
    #driver.find_element(*OrderDifferentButton.CONFIRM_BUTTON).click()
    page_object.confirm_button()

    # Ждем появления кнопки "Посмотреть статус"
    page_object.waiting_status_button()

    # Проверяем, что кнопка отображается
    assert page_object.status_button.is_displayed(), "Кнопка 'Посмотреть статус' не отображается на странице"
