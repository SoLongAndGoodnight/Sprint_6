from pages.main_page import HomePageObject

BASE_URL = "https://qa-scooter.praktikum-services.ru/"

def test_question_time(driver):
    driver.get(BASE_URL)
    driver.maximize_window()
    driver.implicitly_wait(3)

    page_object = HomePageObject(driver)

    # Скролл вниз на 500 пикселей
    for _ in range(4):
        driver.execute_script("window.scrollBy(0, 500);")
        driver.implicitly_wait(1)  # Небольшая пауза после скролла

    page_object.click_question_button_six()

    expected_text = ("Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. "
                     "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. "
                     "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.")

    # ищем ожидаемый текст
    assert expected_text in page_object.element_answer_003.text, f"Текст не найден."