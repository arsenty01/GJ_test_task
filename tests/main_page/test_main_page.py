from pages.main_page import MainPage


def test_01_create_account_pretest(driver, object_factory):
    user = object_factory.create_user_for_login()
    mp = MainPage(driver)
    mp.skip_cookies_banner()
    mp.sign_up()
    mp.fill_signup_form(user)
    mp.check_signup_btn_enabled()


def test_02_localization(driver):
    target_localization = 'de'
    mp = MainPage(driver)
    mp.skip_cookies_banner()
    current_lang = mp.get_current_localization()
    mp.select_language(target_localization)
    new_lang = mp.get_current_localization()
    assert current_lang != new_lang and new_lang == target_localization, "Something went wrong! Language didn't change."








