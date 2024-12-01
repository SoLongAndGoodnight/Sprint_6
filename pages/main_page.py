from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page import (
    QuestionCancel,
    QuestionReturn,
    QuestionOrderToday,
    QuestionCharge,
    QuestionPrice,
    QuestionQuantity,
    QuestionTime,
    QuestionDelivery,
    Redirect,
    MainPageLogoClick
)

from .base import BasePageObject


class HomePageObject(BasePageObject):
    @property
    def element_logo(self):
        return self.driver.find_element(*Redirect.LOGO_REDIRECT)

    def click_logo(self):
        self.element_logo.click()

    @property
    def element_logo_main(self):
        return self.driver.find_element(*MainPageLogoClick.LOGO)

    def click_element_logo_main(self):
        self.element_logo_main.click()

    def find_and_click_question_button(self, text):
        element = self.driver.find_element(By.XPATH, f"//div[contains(text(), '{text}')]")
        element.click()

    def element_paragraph_exists(self, text):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, f"//p[text()='{text}']"))
        )
