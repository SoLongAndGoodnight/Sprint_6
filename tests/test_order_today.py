import time

import allure
from pages.main_page import HomePageObject

BASE_URL = "https://qa-scooter.praktikum-services.ru/"


@allure.title("Проверка ответа на вопрос 'Можно ли заказать самокат прямо на сегодня?'")
def test_question_price(driver):
    driver.get(BASE_URL)
    driver.maximize_window()
    driver.implicitly_wait(3)

    page_object = HomePageObject(driver)

    # Скролл вниз на 500 пикселей
    for _ in range(4):
        driver.execute_script("window.scrollBy(0, 500);")
        driver.implicitly_wait(1)  # Небольшая пауза после скролла
    time.sleep(3)

    #поиск вопроса
    #клик
    page_object.question_order_today_click()

    expected_text = ("Только начиная с завтрашнего дня. Но скоро станем расторопнее.")

    #ищем ожидаемый текст
    assert expected_text in page_object.element_order_today_answer.text, f"Текст не найден."

