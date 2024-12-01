import time
from pages.main_page import HomePageObject

BASE_URL = "https://qa-scooter.praktikum-services.ru/"


def test_question_cancellation(driver):
    driver.get(BASE_URL)
    driver.maximize_window()
    driver.implicitly_wait(3)

    page_object = HomePageObject(driver)

    # Скролл вниз на 700 пикселей
    for _ in range(4):
        driver.execute_script("window.scrollBy(0, 700);")
        driver.implicitly_wait(1)  # Небольшая пауза после скролла
    time.sleep(3)

    #поиск вопроса
    #клик
    page_object.click_question_button()

    expected_text = ("Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.")

    # ищем ожидаемый текст
    assert expected_text in page_object.element_cancel_answer.text, f"Текст не найден."