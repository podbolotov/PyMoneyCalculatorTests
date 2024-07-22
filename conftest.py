import pytest
from conf.capabilities import ApplicationCapabilities
from appium import webdriver
import os


@pytest.fixture(scope="module")
def appium_driver():
    """
    Данная фикстура предоставляет драйвер для взаимодействия с мобильным приложением
    """
    driver_options = ApplicationCapabilities.get()
    appium_server_url = os.environ.get("APPIUM_SERVER") or 'http://localhost:4723'
    driver = webdriver.Remote(
        command_executor=appium_server_url, options=driver_options, )
    driver.implicitly_wait(60)
    yield driver

    driver.quit()
