from selenium.webdriver.common.by import By
from selectors_data import Locators
from expected_data import ExpectedData

selectors_data = Locators()
expected_data = ExpectedData()


def test_error_message_text(set_up):
    set_up.find_element(By.ID, selectors_data.username_id).send_keys(expected_data.username)
    set_up.find_element(By.ID, selectors_data.password_id).send_keys(expected_data.password)
    set_up.find_element(By.CSS_SELECTOR, selectors_data.login_button).click()
    text_displayed = set_up.find_element(By.CSS_SELECTOR, selectors_data.error_displayed).text
    expected = expected_data.text_expected
    # set_up.assertTrue(text_expected in text_displayed, 'Error message text is incorrect')
    assert expected == text_displayed, f'Expected: {expected} . Actual: {text_displayed}'


