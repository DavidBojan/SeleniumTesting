from selenium.webdriver.common.by import By
from selectors_data import Locators
from expected_data import ExpectedData

selector = Locators()
data = ExpectedData()


def test_z_login_logout(set_up):
    set_up.find_element(By.ID, selector.username_id).send_keys(data.username)
    set_up.find_element(By.ID, selector.password_id).send_keys(data.password)
    set_up.find_element(By.CSS_SELECTOR, selector.login_button).click()
    set_up.find_element(By.CSS_SELECTOR, selector.logout).click()
