from selenium.webdriver.common.by import By
from selectors_data import Locators
from expected_data import ExpectedData

selector = Locators()
data = ExpectedData()


def test_brute_force_hacking(set_up):
    passwords_list = set_up.find_element(By.CSS_SELECTOR, selector.target_text).text.split(sep=' ')
    is_found = False
    password_found = None
    for password in range(len(passwords_list)):
        set_up.find_element(By.ID, selector.username_id).send_keys(data.username)
        set_up.find_element(By.ID, selector.password_id).send_keys(passwords_list[password])
        set_up.find_element(By.CSS_SELECTOR, selector.login_button).click()
        actual = set_up.current_url
        expected = 'https://the-internet.herokuapp.com/secure'
        if actual == expected:
            is_found = True
            password_found = passwords_list[password]
            break
        else:
            continue
    if is_found:
        print(f"The secret password is: {password_found}")
    else:
        print("Password not found")
