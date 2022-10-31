from selenium.webdriver.common.by import By
from selectors_data import Locators

selectors_data = Locators()


def test_error_displayed(set_up):
    set_up.find_element(By.CSS_SELECTOR, selectors_data.login_button).click()
    error_display = set_up.find_element(By.CSS_SELECTOR, selectors_data.error_displayed).is_displayed()
    assert error_display, 'Error is not displayed'
