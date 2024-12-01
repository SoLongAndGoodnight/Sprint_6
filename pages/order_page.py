from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.order_page import OrderDifferentButton


class OrderPageObject:

    def __init__(self, driver_):
        self.driver = driver_

    @property
    def name_field(self):
        return self.driver.find_element(*OrderDifferentButton.NAME)

    def name_fill(self, name):
        self.name_field.send_keys(name)

    def surname_fill(self, surname):
        self.driver.find_element(*OrderDifferentButton.LAST_NAME).send_keys(surname)

    def address_fill(self, address):
        self.driver.find_element(*OrderDifferentButton.ADDRESS).send_keys(address)

    def subway_dropdown_click(self):
        self.driver.find_element(*OrderDifferentButton.SUBWAY_FIELD).click()

    def subway_select(self):
        self.driver.find_element(*OrderDifferentButton.SUBWAY_SELECT).click()

    def phone_fill(self, phone):
        self.driver.find_element(*OrderDifferentButton.PHONE).send_keys(phone)

    def dalee_button(self):
        self.driver.find_element(*OrderDifferentButton.DALEE_BUTTON).click()

    def calendar_click(self):
        self.driver.find_element(*OrderDifferentButton.CALENDAR).click()

    def calendar_select(self):
        self.driver.find_element(*OrderDifferentButton.CALENDAR_SELECT).click()

    def rent_click(self):
        self.driver.find_element(*OrderDifferentButton.RENT_DAYS).click()

    def rent_select(self):
        self.driver.find_element(*OrderDifferentButton.RENT_DAYS_SELECT).click()

    def color_click(self):
        self.driver.find_element(*OrderDifferentButton.COLOR).click()

    def order_button(self):
        self.driver.find_element(*OrderDifferentButton.ORDER_BUTTON).click()

    def confirm_button(self):
        self.driver.find_element(*OrderDifferentButton.CONFIRM_BUTTON).click()

    @property
    def status_button(self):
        return self.driver.find_element(*OrderDifferentButton.STATUS_BUTTON)

    def waiting_status_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(OrderDifferentButton.STATUS_BUTTON)
        )

    def upper_order_button_click(self):
        return self.driver.find_element(*OrderDifferentButton.UPPER_BUTTON).click()

    def bottom_order_button_click(self):
        return self.driver.find_element(*OrderDifferentButton.BOTTOM_BUTTON).click()
