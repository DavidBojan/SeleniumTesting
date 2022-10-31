from selenium.webdriver.common.by import By
from selectors_data import Locators
from expected_data import ExpectedData

selectors_data = Locators()
expected_data = ExpectedData()


def test_href_attribute(set_up):
    attribute_link = set_up.find_element(By.CSS_SELECTOR, selectors_data.href_expected).get_attribute('href')
    expected = expected_data.expected_link
    assert expected == attribute_link, f'Expected href: {expected} . Actual: {attribute_link}'
