import os

import pytest
from webdriver_manager.chrome import ChromeType, ChromeDriverManager
from selenium import webdriver
from utils.factory import ObjectFactory


@pytest.fixture()
def driver() -> webdriver:
    is_remote = os.getenv("Remote")
    # for this task I will put it here, for bigger projects - better to move it into config.py
    url = "https://crossout.net/en/play4free"

    # init driver object for this task I will use settings only for chrome after we can split it for any we need
    options = webdriver.ChromeOptions()
    # for now just make it silent
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("-disable-dev-shm-usage")
    if is_remote:
        driver = webdriver.Remote(command_executor='http://selenoid:4444/wd/hub', options=options)
    else:
        service = webdriver.chrome.service.Service(
                executable_path=ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install()
        )
        driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture()
def object_factory() -> ObjectFactory:
    yield ObjectFactory()
    # here should be method to clean up database/system from created data
    # but I don't have access to DB itself and delete it via UI is bad practice
