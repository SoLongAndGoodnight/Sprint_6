from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.order_page import OrderDifferentButton


class OrderPageObject:
    def __init__(self, driver_):
        self.driver = driver_

    @property
    def element_name(self):
        return self.driver.find_element(*OrderDifferentButton.NAME)

    def name_fill(self, name):
        self.element_name.send_keys(name)

    @property
    def element_surname(self):
        return self.driver.find_element(*OrderDifferentButton.SURNAME)

    def surname_fill(self, surname):
        self.element_surname.send_keys(surname)

    @property
    def element_address(self):
        return self.driver.find_element(*OrderDifferentButton.ADDRESS)

    def address_fill(self, address):
        self.element_address.send_keys(address)

    @property
    def element_dropdown(self):
        return self.driver.find_element(*OrderDifferentButton.SUBWAY_FIELD)

    def subway_dropdown_click(self):
        self.element_dropdown.click()

    @property
    def element_subway(self):
        return self.driver.find_element(*OrderDifferentButton.SUBWAY_SELECT)

    def subway_select(self):
        self.element_subway.click()

    @property
    def element_phone(self):
        return self.driver.find_element(*OrderDifferentButton.PHONE)

    def phone_fill(self, phone):
        self.element_phone.send_keys(phone)

    @property
    def next_button(self):
        return self.driver.find_element(*OrderDifferentButton.NEXT_BUTTON)

    def next_button_click(self):
        self.next_button.click()

    @property
    def element_calendar(self):
        return self.driver.find_element(*OrderDifferentButton.CALENDAR)

    def calendar_click(self):
        self.element_calendar.click()

    @property
    def element_calendar_select(self):
        return self.driver.find_element(*OrderDifferentButton.CALENDAR_SELECT)

    def calendar_select(self):
        self.element_calendar_select.click()

    @property
    def element_rent_days(self):
        return self.driver.find_element(*OrderDifferentButton.RENT_DAYS)

    def rent_click(self):
        self.element_rent_days.click()

    @property
    def element_rent_days_select(self):
        return self.driver.find_element(*OrderDifferentButton.RENT_DAYS_SELECT)

    def rent_days_select_click(self):
        self.element_rent_days_select.click()

    @property
    def element_color(self):
        return self.driver.find_element(*OrderDifferentButton.COLOR)

    def color_click(self):
        self.element_color.click()

    @property
    def element_order_button(self):
        return self.driver.find_element(*OrderDifferentButton.ORDER_BUTTON)

    def order_button_click(self):
        self.element_order_button.click()

    @property
    def element_confirm_button(self):
        return self.driver.find_element(*OrderDifferentButton.CONFIRM_BUTTON)

    def confirm_button_click(self):
        self.element_confirm_button.click()

    @property
    def status_button(self):
        return self.driver.find_element(*OrderDifferentButton.STATUS_BUTTON)

    def waiting_status_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(OrderDifferentButton.STATUS_BUTTON)
        )

    @property
    def element_upper_order_button(self):
        return self.driver.find_element(*OrderDifferentButton.UPPER_BUTTON)

    def upper_order_button_click(self):
        self.element_upper_order_button.click()

    @property
    def element_bottom_order_button(self):
        return self.driver.find_element(*OrderDifferentButton.BOTTOM_BUTTON)

    def bottom_order_button_click(self):
        self.element_bottom_order_button.click()