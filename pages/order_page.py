from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrderPageObject:
    NAME = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    LAST_NAME = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    ADDRESS = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    SUBWAY_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
    SUBWAY_SELECT = (By.CSS_SELECTOR, ".select-search__options [data-index='1']")
    PHONE = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")
    DALEE_BUTTON = (By.XPATH, "//button[contains(text(), 'Далее')]")
    CALENDAR = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
    CALENDAR_SELECT = (By.XPATH, "//div[@aria-label='Choose воскресенье, 1-е декабря 2024 г.']")
    RENT_DAYS = (By.XPATH, "//div[text()='* Срок аренды']")
    RENT_DAYS_SELECT = (By.XPATH, "//div[text()='трое суток']")
    COLOR = (By.ID, "black")
    ORDER_BUTTON = (By.XPATH, "//div[3]/button[2][text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//div[2]/button[2][text()='Да']")
    STATUS_BUTTON = (By.XPATH, '//button[text()="Посмотреть статус"]')
    UPPER_BUTTON = (By.CSS_SELECTOR, ".Button_Button__ra12g")
    BOTTOM_BUTTON = (By.CSS_SELECTOR, ".Button_Middle__1CSJM")


    def __init__(self, driver_):
        self.driver = driver_

    @property
    def name_field(self):
        return self.driver.find_element(*self.NAME)

    def name_fill(self, name):
        self.name_field.send_keys(name)

    def surname_fill(self, surname):
        self.driver.find_element(*self.LAST_NAME).send_keys(surname)

    def address_fill(self, address):
        self.driver.find_element(*self.ADDRESS).send_keys(address)

    def subway_dropdown_click(self):
        self.driver.find_element(*self.SUBWAY_FIELD).click()

    def subway_select(self):
        self.driver.find_element(*self.SUBWAY_SELECT).click()

    def phone_fill(self, phone):
        self.driver.find_element(*self.PHONE).send_keys(phone)

    def dalee_button(self):
        self.driver.find_element(*self.DALEE_BUTTON).click()

    def calendar_click(self):
        self.driver.find_element(*self.CALENDAR).click()

    def calendar_select(self):
        self.driver.find_element(*self.CALENDAR_SELECT).click()

    def rent_click(self):
        self.driver.find_element(*self.RENT_DAYS).click()

    def rent_select(self):
        self.driver.find_element(*self.RENT_DAYS_SELECT).click()

    def color_click(self):
        self.driver.find_element(*self.COLOR).click()

    def order_button(self):
        self.driver.find_element(*self.ORDER_BUTTON).click()

    def confirm_button(self):
        self.driver.find_element(*self.CONFIRM_BUTTON).click()


    @property
    def status_button(self):
        return self.driver.find_element(*self.STATUS_BUTTON)

    def waiting_status_button(self):
        status_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.STATUS_BUTTON)
        )

    def upper_order_button_click(self):
        return self.driver.find_element(*self.UPPER_BUTTON).click()

    def bottom_order_button_click(self):
        return self.driver.find_element(*self.BOTTOM_BUTTON).click()




