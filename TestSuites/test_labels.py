from selenium.webdriver.common.by import By
from selectors_data import Locators
from expected_data import ExpectedData
import selenium

selectors = Locators()
expected = ExpectedData()


def test_labels(set_up):
    user_label = set_up.find_elements(By.CSS_SELECTOR, selectors.label)
    expected0 = expected.user_label
    assert expected0 == user_label[0].text, f'Expected user label: {expected0} . Actual: {user_label[0].text}'
    expected1 = expected.password_label
    assert expected1 == user_label[1].text, f'Expected password label: {expected1} . Actual: {user_label[1].text}'
