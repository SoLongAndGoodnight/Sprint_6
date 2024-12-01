import time

from pages.main_page import HomePageObject
import allure


@allure.title("Вы привозите зарядку вместе с самокатом?'")
def test_question_charge(driver, main_page_url):
    driver.get(main_page_url)
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
    page_object.question_charge_click()

    expected_text = ("Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь "
                     "суток — даже если будете кататься без передышек и во сне. "
                     "Зарядка не понадобится.")

    # ищем ожидаемый текст
    assert expected_text in page_object.element_charge_answer.text, f"Текст не найден."