from selenium.webdriver.common.by import By


class HomePageObject:
    question_button = (By.XPATH, "//div[@id='accordion__heading-6' and @class='accordion__button']")
    question_button_one = (By.XPATH, "//div[@id='accordion__heading-4' and @class='accordion__button']")
    question_button_two = (By.XPATH, "//div[@id='accordion__heading-3' and @class='accordion__button']")
    question_button_three = (By.XPATH, "//div[@id='accordion__heading-5' and @class='accordion__button']")
    question_button_four = (By.XPATH, "//div[@id='accordion__heading-0' and @class='accordion__button']")
    question_button_five = (By.XPATH, "//div[@id='accordion__heading-1' and @class='accordion__button']")
    question_button_six = (By.XPATH, "//div[@id='accordion__heading-2' and @class='accordion__button']")
    question_button_seven = (By.XPATH, "//div[@id='accordion__heading-7' and @class='accordion__button']")
    logo_button = (By.CSS_SELECTOR, "a[href='//yandex.ru']")
    logo_main_button = (By.XPATH, "//*[@class='Header_Logo__23yGT']")
    answer = (By.XPATH, "//p[text()='Да, обязательно. Всем самокатов! И Москве, и Московской области.']")
    answer_002 = (By.XPATH, "//p[text()='Сутки — 400 рублей. Оплата курьеру — наличными или картой.']")
    answer_003 = (By.XPATH,"//p[text()='Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. "
                     "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. "
                     "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.']")
    answer_004 = (By.XPATH,"//p[text()='Пока что у нас так: один заказ — один самокат. "
                       "Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']")
    answer_005 = (By.XPATH, "//p[text()='Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь "
                        "суток — даже если будете кататься без передышек и во сне. "
                        "Зарядка не понадобится.']")
    answer_006 = (By.XPATH,"//p[text()='Да, пока самокат не привезли. "
        "Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']")
    answer_007 = (By.XPATH, "//p[text()='Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.']")
    answer_008 = (By.XPATH,"//p[text()='Только начиная с завтрашнего дня. Но скоро станем расторопнее.']")


    def __init__(self, driver_):
        self.driver = driver_

    @property
    def element_question_button(self):
        return self.driver.find_element(*self.question_button)

    def click_question_button(self):
        self.element_question_button.click()

    @property
    def element_question_button_one(self):
        return self.driver.find_element(*self.question_button_one)

    def click_question_button_one(self):
        self.element_question_button_one.click()

    @property
    def element_question_button_two(self):
        return self.driver.find_element(*self.question_button_two)

    def click_question_button_two(self):
        self.element_question_button_two.click()

    @property
    def element_question_button_three(self):
        return self.driver.find_element(*self.question_button_three)

    def click_question_button_three(self):
        self.element_question_button_three.click()

    @property
    def element_question_button_four(self):
        return self.driver.find_element(*self.question_button_four)

    def click_question_button_four(self):
        self.element_question_button_four.click()

    @property
    def element_question_button_five(self):
        return self.driver.find_element(*self.question_button_five)

    def click_question_button_five(self):
        self.element_question_button_five.click()

    @property
    def element_question_six(self):
        return self.driver.find_element(*self.question_button_six)

    def click_question_button_six(self):
        self.element_question_six.click()

    @property
    def element_logo(self):
        return self.driver.find_element(*self.logo_button)

    def click_logo(self):
        self.element_logo.click()

    @property
    def element_question_seven(self):
        return self.driver.find_element(*self.question_button_seven)

    def click_question_button_seven(self):
        self.element_question_seven.click()

    @property
    def element_logo_main(self):
        return self.driver.find_element(*self.logo_main_button)

    def click_element_logo_main(self):
        self.element_logo_main.click()

    @property
    def element_answer(self):
        return self.driver.find_element(*self.answer)

    @property
    def element_answer_002(self):
        return self.driver.find_element(*self.answer_002)

    @property
    def element_answer_003(self):
        return self.driver.find_element(*self.answer_003)

    @property
    def element_answer_004(self):
        return self.driver.find_element(*self.answer_004)

    @property
    def element_answer_005(self):
        return self.driver.find_element(*self.answer_005)

    @property
    def element_answer_006(self):
        return self.driver.find_element(*self.answer_006)

    @property
    def element_answer_007(self):
        return self.driver.find_element(*self.answer_007)

    @property
    def element_answer_008(self):
        return self.driver.find_element(*self.answer_008)

