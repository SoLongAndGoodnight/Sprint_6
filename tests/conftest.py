import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    # Создание экземпляра WebDriver
    driver = webdriver.Firefox()  # или webdriver.Firefox() в зависимости от вашего браузера
    driver.maximize_window()

    yield driver  # Возвращаем драйвер тесту и приостанавливаем фикстуру

    # Завершение работы драйвера после выполнения теста
    driver.quit()


@pytest.fixture
def main_page_url():
    return "https://qa-scooter.praktikum-services.ru/"


@pytest.fixture
def order_page_url():
    return "https://qa-scooter.praktikum-services.ru/order"
