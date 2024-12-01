from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGO = (By.XPATH, "//*[@class='Header_Logo__23yGT']")
    LOGO_REDIRECT = (By.CSS_SELECTOR, "a[href='//yandex.ru']")
