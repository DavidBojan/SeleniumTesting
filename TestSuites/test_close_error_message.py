from selenium.webdriver.common.by import By
from selectors_data import Locators

selectors_data = Locators()


def test_close_error_message(set_up):

    set_up.find_element(By.CSS_SELECTOR, selectors_data.login_button).click()
    set_up.find_element(By.CSS_SELECTOR, selectors_data.close_error).click()
    error_display = set_up.find_element(By.CSS_SELECTOR, selectors_data.error_displayed).is_displayed()
    assert error_display, 'Error is not displayed'
