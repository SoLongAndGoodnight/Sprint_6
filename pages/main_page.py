from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderForm:
    NAME_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    SUBWAY_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
    SUBWAY_STATION = (By.XPATH, ".//div[@class='select-search__select']/ui/li[1]/button/div[2]")
    FIRST_BUTTON = (By.CSS_SELECTOR, ".Button_Button__ra12g")

