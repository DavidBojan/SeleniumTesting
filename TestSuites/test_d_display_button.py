from selenium.webdriver.common.by import By


def test_display_button(set_up):
    login_button = set_up.find_element(By.CLASS_NAME, 'radius').is_displayed()
    assert login_button, 'Login button is not displayed'
