import pytest
from selenium import webdriver

@pytest.fixture
#def driver():
    #return webdriver.Chrome()
    #driver.maximize_window()
    #yield
    #


def driver():
    # Создание экземпляра WebDriver
    driver = webdriver.Firefox()  # или webdriver.Firefox() в зависимости от вашего браузера
    driver.maximize_window()
    yield driver  # Возвращаем драйвер тесту и приостанавливаем фикстуру

    # Завершение работы драйвера после выполнения теста
    driver.quit()