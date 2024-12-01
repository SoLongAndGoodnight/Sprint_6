from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from pages.main_page import HomePageObject

BASE_URL = "https://qa-scooter.praktikum-services.ru/"


@allure.title("Проверка редиректа на dzen")
def test_redirect(driver):
    driver.get(BASE_URL)
    driver.implicitly_wait(3)

    page_object = HomePageObject(driver)

    page_object.click_logo()

    # Переключаемся на новую вкладку, если редирект открывает её
    driver.switch_to.window(driver.window_handles[-1])

    #ожидание редиректа
    WebDriverWait(driver, 5).until(
        EC.url_contains("dzen.ru"),
        message="Ожидание URL с 'dzen.ru' истекло"
    )

    # Проверяем, что редирект состоялся
    assert "dzen.ru" in driver.current_url, f"Редирект не состоялся, текущий URL: {driver.current_url}"