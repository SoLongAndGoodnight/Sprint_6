from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.order_page import OrderPageLocators

from .base import BasePageObject


class OrderPageObject(BasePageObject):
    @property
    def element_name(self):
        return self.driver.find_element(*OrderPageLocators.NAME)

    def name_fill(self, name):
        self.element_name.send_keys(name)

    @property
    def element_surname(self):
        return self.driver.find_element(*OrderPageLocators.SURNAME)

    def surname_fill(self, surname):
        self.element_surname.send_keys(surname)

    @property
    def element_address(self):
        return self.driver.find_element(*OrderPageLocators.ADDRESS)

    def address_fill(self, address):
        self.element_address.send_keys(address)

    @property
    def element_dropdown(self):
        return self.driver.find_element(*OrderPageLocators.SUBWAY_FIELD)

    def subway_dropdown_click(self):
        self.element_dropdown.click()

    @property
    def element_subway(self):
        return self.driver.find_element(*OrderPageLocators.SUBWAY_SELECT)

    def subway_select(self):
        self.element_subway.click()

    @property
    def element_phone(self):
        return self.driver.find_element(*OrderPageLocators.PHONE)

    def phone_fill(self, phone):
        self.element_phone.send_keys(phone)

    @property
    def next_button(self):
        return self.driver.find_element(*OrderPageLocators.NEXT_BUTTON)

    def next_button_click(self):
        self.next_button.click()

    @property
    def element_calendar(self):
        return self.driver.find_element(*OrderPageLocators.CALENDAR)

    def calendar_click(self):
        self.element_calendar.click()

    @property
    def element_calendar_select(self):
        return self.driver.find_element(*OrderPageLocators.CALENDAR_SELECT)

    def calendar_select(self):
        self.element_calendar_select.click()

    @property
    def element_rent_days(self):
        return self.driver.find_element(*OrderPageLocators.RENT_DAYS)

    def rent_click(self):
        self.element_rent_days.click()

    @property
    def element_rent_days_select(self):
        return self.driver.find_element(*OrderPageLocators.RENT_DAYS_SELECT)

    def rent_days_select_click(self):
        self.element_rent_days_select.click()

    @property
    def element_color(self):
        return self.driver.find_element(*OrderPageLocators.COLOR)

    def color_click(self):
        self.element_color.click()

    @property
    def element_order_button(self):
        return self.driver.find_element(*OrderPageLocators.ORDER_BUTTON)

    def order_button_click(self):
        self.element_order_button.click()

    @property
    def element_confirm_button(self):
        return self.driver.find_element(*OrderPageLocators.CONFIRM_BUTTON)

    def confirm_button_click(self):
        self.element_confirm_button.click()

    @property
    def status_button(self):
        return self.driver.find_element(*OrderPageLocators.STATUS_BUTTON)

    def waiting_status_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(OrderPageLocators.STATUS_BUTTON)
        )

    @property
    def element_upper_order_button(self):
        return self.driver.find_element(*OrderPageLocators.UPPER_BUTTON)

    def upper_order_button_click(self):
        self.element_upper_order_button.click()

    @property
    def element_bottom_order_button(self):
        return self.driver.find_element(*OrderPageLocators.BOTTOM_BUTTON)

    def bottom_order_button_click(self):
        self.element_bottom_order_button.click()