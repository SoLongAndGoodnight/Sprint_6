from selenium.webdriver.common.by import By


class OrderDifferentButton:
    NAME = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    SURNAME = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    ADDRESS = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    SUBWAY_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
    SUBWAY_SELECT = (By.CSS_SELECTOR, ".select-search__options [data-index='1']")
    PHONE = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(), 'Далее')]")
    CALENDAR = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
    CALENDAR_SELECT = (By.XPATH, "//div[@aria-label='Choose воскресенье, 1-е декабря 2024 г.']")
    RENT_DAYS = (By.XPATH, "//div[text()='* Срок аренды']")
    RENT_DAYS_SELECT = (By.XPATH, "//div[text()='трое суток']")
    COLOR = (By.ID, "black")
    # на странице 2 кнопки "Заказать", поэтому ищем кнопку через блок контента
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons__1xGrp')]//button[contains(text(), 'Заказать')]")
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(), 'Да')]")
    STATUS_BUTTON = (By.XPATH, '//button[text()="Посмотреть статус"]')
    UPPER_BUTTON = (By.CSS_SELECTOR, ".Button_Button__ra12g")
    BOTTOM_BUTTON = (By.CSS_SELECTOR, ".Button_Middle__1CSJM")
