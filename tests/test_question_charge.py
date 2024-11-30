import time

from pages.main_page import HomePageObject

BASE_URL = "https://qa-scooter.praktikum-services.ru/"

def test_question_charge(driver):
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
    #question_charge.click()
    page_object.click_question_button_three()

    expected_text = ("Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь "
                     "суток — даже если будете кататься без передышек и во сне. "
                     "Зарядка не понадобится.")

    # ищем ожидаемый текст
    assert expected_text in page_object.element_answer_005.text, f"Текст не найден."