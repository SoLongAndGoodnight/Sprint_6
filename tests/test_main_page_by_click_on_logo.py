from pages.main_page import HomePageObject

BASE_URL = "https://qa-scooter.praktikum-services.ru/order"


def test_main_page_by_click_on_logo(driver):
    driver.get(BASE_URL)
    driver.implicitly_wait(3)

    page_object = HomePageObject(driver)

    # ищем лого и кликаем
    page_object.click_element_logo_main()

    #ищем на главной странице модуль и провеляем его отображение
    assert page_object.element_logo_main.is_displayed()
