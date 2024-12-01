import time

from pages.main_page import HomePageObject

BASE_URL = "https://qa-scooter.praktikum-services.ru/"


def test_question_price(driver):
    driver.get(BASE_URL)
    driver.maximize_window()
    driver.implicitly_wait(3)

    page_object = HomePageObject(driver)

    # Прокручиваем до вопроса
    for _ in range(4):
        driver.execute_script("window.scrollBy(0, 500);")  # Скролл вниз на 500 пикселей
        driver.implicitly_wait(1)  # Небольшая пауза после скролла
    time.sleep(3)

    # Кликаем на элемент
    #price.click()
    page_object.click_question_button_four()

    # Ищем текст, который должен отобразиться после клика
    expected_text = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    # Проверяем, что текст отобразился на странице
    assert expected_text in page_object.element_price_answer.text, f"Текст не найден."
