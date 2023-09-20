from selenium.webdriver.common.by import By
from utils.factory import User
from .region import Region  # somehow didn't work without "."


class MainPage(Region):
    """
        main page class
    """

    LOGIN_BTN = (By.CSS_SELECTOR, ".land__buttons-play .button--play")

    # language combobox
    LANGUAGE_CMBX = (By.CSS_SELECTOR, ".lang-picker__switcher")
    LANGUAGE_LIST_LINE = (By.CSS_SELECTOR, ".lang-picker__link")

    # cookies banner
    BANNER_CONTAINER = (By.CSS_SELECTOR, "[data-cookiefirst-widget='banner']")
    ACCEPT_ALL_BTN = (By.CSS_SELECTOR, "[data-cookiefirst-action='accept']")

    # login popup
    SIGNUP_FORM_CONTAINER = (By.CSS_SELECTOR, ".form-container--signup")
    EMAIL_INP = (By.NAME, "login")
    NICKNAME_INP = (By.NAME, "nick")
    PASSWORD_INP = (By.NAME, "password")
    PASSWORD_RPT_INP = (By.NAME, "passwordRepeat")
    CAPTCHA_INP = (By.NAME, "captcha")
    EULA_CHKBX = (By.CSS_SELECTOR, "[for='eulaagree'] span")
    SUBMIT_BTN = (By.CSS_SELECTOR, "[value='Create an account']")
    SUBMIT_BTN_FAKE = (By.CSS_SELECTOR, "[data-test-id='button-registration-fake']")

    def skip_cookies_banner(self):
        self.dummy_wait()  # bad practice, but I don't have any details abt project ;)
        self.is_visible(self.BANNER_CONTAINER)
        self.wait(self.ACCEPT_ALL_BTN).click()
        self.not_visible(self.BANNER_CONTAINER)

    def sign_up(self):
        self.wait(self.LOGIN_BTN).click()
        self.is_visible(self.SIGNUP_FORM_CONTAINER)

    def fill_signup_form(self, user: User):
        self.is_visible(self.SIGNUP_FORM_CONTAINER)
        self.wait(self.EMAIL_INP).send_keys(user.email)
        self.wait(self.NICKNAME_INP).send_keys(user.nickname)
        self.wait(self.PASSWORD_INP).send_keys(user.password)
        self.wait(self.PASSWORD_RPT_INP).send_keys(user.password)
        self.wait(self.CAPTCHA_INP).send_keys(user.captcha)
        self.wait(self.EULA_CHKBX).click()

    def check_signup_btn_enabled(self):
        self.dummy_wait()  # bad practice, but I don't have any details abt project ;)
        assert self.not_visible(self.SUBMIT_BTN_FAKE), 'Something went wrong - signup button is disabled!'

    def select_language(self, target_lang: str):
        self.wait(self.LANGUAGE_CMBX).click()
        target_lang_locator = (By.CSS_SELECTOR, f"[data-test-id='link-lang-picker-{target_lang}']")
        self.wait(target_lang_locator).click()










