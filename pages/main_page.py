from locators.main_page import (
    QuestionCancel,
    QuestionReturn,
    OrderToday,
    QuestionCharge,
    QuestionPrice,
    QuestionQuantity,
    QuestionTime,
    QuestionDelivery,
    Redirect,
    MainPageLogoClick
)


class HomePageObject:
    def __init__(self, driver_):
        self.driver = driver_

    @property
    def element_question_button(self):
        return self.driver.find_element(*QuestionCancel.QUESTION)

    def click_question_button(self):
        self.element_question_button.click()

    @property
    def element_question_button_one(self):
        return self.driver.find_element(*QuestionReturn.QUESTION)

    def click_question_button_one(self):
        self.element_question_button_one.click()

    @property
    def element_question_button_two(self):
        return self.driver.find_element(*OrderToday.QUESTION)

    def click_question_button_two(self):
        self.element_question_button_two.click()

    @property
    def element_question_button_three(self):
        return self.driver.find_element(*QuestionCharge.QUESTION)

    def click_question_button_three(self):
        self.element_question_button_three.click()

    @property
    def element_question_button_four(self):
        return self.driver.find_element(*QuestionPrice.QUESTION)

    def click_question_button_four(self):
        self.element_question_button_four.click()

    @property
    def element_question_button_five(self):
        return self.driver.find_element(*QuestionQuantity.QUESTION)

    def click_question_button_five(self):
        self.element_question_button_five.click()

    @property
    def element_question_six(self):
        return self.driver.find_element(*QuestionTime.QUESTION)

    def click_question_button_six(self):
        self.element_question_six.click()

    @property
    def element_logo(self):
        return self.driver.find_element(*Redirect.LOGO_REDIRECT)

    def click_logo(self):
        self.element_logo.click()

    @property
    def element_question_seven(self):
        return self.driver.find_element(*QuestionDelivery.QUESTION)

    def click_question_button_seven(self):
        self.element_question_seven.click()

    @property
    def element_logo_main(self):
        return self.driver.find_element(*MainPageLogoClick.LOGO)

    def click_element_logo_main(self):
        self.element_logo_main.click()

    @property
    def element_delivery_answer(self):
        return self.driver.find_element(*QuestionDelivery.ANSWER)

    @property
    def element_price_answer(self):
        return self.driver.find_element(*QuestionPrice.ANSWER)

    @property
    def element_time_answer(self):
        return self.driver.find_element(*QuestionTime.ANSWER)

    @property
    def element_quantity_answer(self):
        return self.driver.find_element(*QuestionQuantity.ANSWER)

    @property
    def element_charge_answer(self):
        return self.driver.find_element(*QuestionCharge.ANSWER)

    @property
    def element_cancel_answer(self):
        return self.driver.find_element(*QuestionCancel.ANSWER)

    @property
    def element_return_answer(self):
        return self.driver.find_element(*QuestionReturn.ANSWER)

    @property
    def element_order_today_answer(self):
        return self.driver.find_element(*OrderToday.ANSWER)

