from pages.main_page import HomePageObject

BASE_URL = "https://qa-scooter.praktikum-services.ru/"


def test_question_quantity(driver):
    driver.get(BASE_URL)
    driver.maximize_window()
    driver.implicitly_wait(3)

    page_object = HomePageObject(driver)

    # Скролл вниз на 500 пикселей
    for _ in range(4):
        driver.execute_script("window.scrollBy(0, 500);")
        driver.implicitly_wait(1)  # Небольшая пауза после скролла

    page_object.click_question_button_five()

    expected_text = ("Пока что у нас так: один заказ — один самокат. "
                     "Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.")

    #ищем ожидаемый текст
    # Проверяем, что текст отобразился на странице
    assert expected_text in page_object.element_quantity_answer.text, f"Текст не найден."
