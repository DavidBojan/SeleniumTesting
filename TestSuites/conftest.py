import pytest
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='session', autouse=True)
def set_up():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://the-internet.herokuapp.com/login')
    driver.maximize_window()
    yield driver
    driver.quit()
