from selenium.webdriver.common.by import By
from expected_data import ExpectedData

expected_data = ExpectedData()


def test_element_text(set_up):
    page_title = set_up.find_element(By.CSS_SELECTOR, 'div>h2').text
    expected = expected_data.title_expected
    assert expected == page_title, f'Expected title: {expected} . Actual: {page_title}'
