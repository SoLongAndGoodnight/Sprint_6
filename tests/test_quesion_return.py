from pages.main_page import HomePageObject

BASE_URL = "https://qa-scooter.praktikum-services.ru/"


def test_question_return(driver):
    driver.get(BASE_URL)
    driver.maximize_window()
    driver.implicitly_wait(3)

    page_object = HomePageObject(driver)

    # Скролл вниз на 700 пикселей
    for _ in range(4):
        driver.execute_script("window.scrollBy(0, 700);")
        driver.implicitly_wait(1)  # Небольшая пауза после скролла

    page_object.click_question_button_one()

    expected_text = ("Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.")

    # ищем ожидаемый текст
    assert expected_text in page_object.element_answer_007.text, f"Текст не найден."