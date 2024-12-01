from selenium.webdriver.common.by import By


class MainPageLogoClick:
    LOGO = (By.XPATH, "//*[@class='Header_Logo__23yGT']")


class QuestionOrderToday:
    QUESTION = (By.XPATH, "//div[@id='accordion__heading-3' and @class='accordion__button']")
    ANSWER = (By.XPATH, "//p[text()='Только начиная с завтрашнего дня. Но скоро станем расторопнее.']")


class QuestionReturn:
    QUESTION = (By.XPATH, "//div[@id='accordion__heading-4' and @class='accordion__button']")
    ANSWER = (By.XPATH, "//p[text()='Пока что нет! Но если что-то срочное — "
                        "всегда можно позвонить в поддержку по красивому номеру 1010.']")


class QuestionCancel:
    QUESTION = (By.XPATH, "//div[@id='accordion__heading-6' and @class='accordion__button']")
    ANSWER = (By.XPATH, "//p[text()='Да, пока самокат не привезли. "
        "Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']")


class QuestionCharge:
    QUESTION = (By.XPATH, "//div[@id='accordion__heading-5' and @class='accordion__button']")
    ANSWER = (By.XPATH, "//p[text()='Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь "
    "суток — даже если будете кататься без передышек и во сне. "
    "Зарядка не понадобится.']")


class QuestionPrice:
    QUESTION = (By.XPATH, "//div[@id='accordion__heading-0' and @class='accordion__button']")
    ANSWER = (By.XPATH, "//p[text()='Сутки — 400 рублей. Оплата курьеру — наличными или картой.']")


class QuestionQuantity:
    QUESTION = (By.XPATH, "//div[@id='accordion__heading-1' and @class='accordion__button']")
    ANSWER = (By.XPATH, "//p[text()='Пока что у нас так: один заказ — один самокат. "
                       "Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']")


class QuestionTime:
    QUESTION = (By.XPATH, "//div[@id='accordion__heading-2' and @class='accordion__button']")
    ANSWER = (By.XPATH, "//p[text()='Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. "
                     "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. "
                     "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.']")


class Redirect:
    LOGO_REDIRECT = (By.CSS_SELECTOR, "a[href='//yandex.ru']")


class QuestionDelivery:
    QUESTION = (By.XPATH, "//div[@id='accordion__heading-7' and @class='accordion__button']")
    ANSWER = (By.XPATH, "//p[text()='Да, обязательно. Всем самокатов! И Москве, и Московской области.']")
