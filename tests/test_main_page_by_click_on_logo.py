from pages.main_page import HomePageObject
import allure

BASE_URL = "https://qa-scooter.praktikum-services.ru/order"


@allure.title("Проверка перехода на main page по клику на логотип")
def test_main_page_by_click_on_logo(driver):
    driver.get(BASE_URL)
    driver.implicitly_wait(3)

    page_object = HomePageObject(driver)

    page_object.click_element_logo_main()

    assert page_object.element_logo_main.is_displayed()
