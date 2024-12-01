import time

import allure
import pytest
from pages.order_page import OrderPageObject

BASE_URL = "https://qa-scooter.praktikum-services.ru/"


@allure.title("Проверка заказа самоката с разных точек входа")
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

    # Заполняем модальник заказа
    # Заполняем имя
    page_object.name_fill(name)

    # Заполняем фамилию
    page_object.surname_fill(surname)

    # Заполняем адрес
    page_object.address_fill(address)

    # Клик на поле с метро
    page_object.subway_dropdown_click()

    page_object.subway_select()

    # Заполняем телефон
    page_object.phone_fill(phone)

    # Нажимаем кнопку "Далее"
    page_object.next_button_click()

    # Заполняем календарь
    page_object.calendar_click()

    page_object.calendar_select()

    # Указываем срок аренды
    page_object.rent_click()

    page_object.rent_days_select_click()

    # Выбираем цвет
    page_object.color_click()

    # Клик на кнопку "Заказать"
    page_object.order_button_click()

    # Подтверждение заказа
    page_object.confirm_button_click()

    # Ждем появления кнопки "Посмотреть статус"
    page_object.waiting_status_button()

    # Проверяем, что кнопка отображается
    assert page_object.status_button.is_displayed(), "Кнопка 'Посмотреть статус' не отображается на странице"
