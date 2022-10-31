from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException


def test_login_secure_and_element_display(set_up):
    set_up.find_element(By.NAME, 'username').send_keys('tomsmith')
    set_up.find_element(By.NAME, 'password').send_keys('SuperSecretPassword!')
    set_up.find_element(By.CLASS_NAME, 'radius').click()
    actual = set_up.current_url
    expected = 'https://the-internet.herokuapp.com/secure'
    assert expected == actual, 'URL is incorrect'
    try:
        wait = WebDriverWait(set_up, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.ID, 'flash')))
        wait.until(expected_conditions.text_to_be_present_in_element((By.ID, 'flash'), 'secure area!'))
    except TimeoutException:
        return False
    return True
