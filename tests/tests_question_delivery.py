import time

import allure
from pages.main_page import HomePageObject


@allure.title("Ответ на вопрос 'Я жизу за МКАДом, привезёте?'")
def test_question_delivery(driver, main_page_url):
    driver.get(main_page_url)
    driver.maximize_window()
    driver.implicitly_wait(3)

    page_object = HomePageObject(driver)

    # Скролл вниз на 700 пикселей
    for _ in range(4):
        driver.execute_script("window.scrollBy(0, 700);")
        driver.implicitly_wait(1)  # Небольшая пауза после скролла
    time.sleep(3)

    page_object.click_question_button_seven()

    expected_text = ("Да, обязательно. Всем самокатов! И Москве, и Московской области.")

    # ищем ожидаемый текст
    assert expected_text in page_object.element_delivery_answer.text, f"Текст не найден."