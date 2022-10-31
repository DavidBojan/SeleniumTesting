from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

import unittest


class Login(unittest.TestCase):
    # se ruleaza inainte de fiecare test
    def setUp(self):
        self.chrome = webdriver.Chrome(ChromeDriverManager().install())
        self.chrome.maximize_window()
        # yield self.chrome
        self.chrome.get('https://the-internet.herokuapp.com/login')

    # se ruleaza dupa fiecare test
    def tearDown(self):
        self.chrome.quit()

    def test_url(self):
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        # expected value, actual value, mesaj in caz de fail
        self.assertEqual(expected, actual, 'URL is incorrect')

    def test_page_title(self):
        page_title = self.chrome.title
        title_expected = 'The Internet'
        self.assertEqual(title_expected, page_title, 'Page title is incorrect')

    def test_element_text(self):
        page_title = self.chrome.find_element(By.XPATH, '//div[@id="content"]/div/h2').text
        title_expected = 'Login Page'
        self.assertEqual(title_expected, page_title, 'Element text is incorrect')

    def test_display_button(self):
        login_button = self.chrome.find_element(By.CLASS_NAME, 'radius').is_displayed()
        assert login_button, 'Login button is not displayed'

    def test_href_attribute(self):
        attribute_link = self.chrome.find_element(By.LINK_TEXT, 'Elemental Selenium').get_attribute('href')
        expected_link = 'http://elementalselenium.com/'
        self.assertEqual(attribute_link, expected_link, 'Actual href link is incorrect')

    def test_error_displayed(self):
        self.chrome.find_element(By.CLASS_NAME, 'radius').click()
        error_display = self.chrome.find_element(By.ID, 'flash').is_displayed()
        assert error_display, 'Error is not displayed'

    def test_error_message_text(self):
        self.chrome.find_element(By.ID, 'username').send_keys('johndoe')
        self.chrome.find_element(By.ID, 'password').send_keys('NotASuperPass?')
        self.chrome.find_element(By.CLASS_NAME, 'radius').click()
        text_displayed = self.chrome.find_element(By.ID, 'flash').text
        text_expected = 'Your username is invalid!'
        self.assertTrue(text_expected in text_displayed, 'Error message text is incorrect')

    def test_close_error_message(self):
        self.chrome.find_element(By.CLASS_NAME, 'radius').click()
        self.chrome.find_element(By.XPATH, "//a[contains(text(),'×')]").click()
        self.test_error_displayed()

    def test_labels(self):
        label_list = self.chrome.find_elements(By.XPATH, '//label')

        expected_label0 = 'Username'
        self.assertEqual(label_list[0].text, expected_label0,
                         f'Expected label: {expected_label0}. Actual label: {label_list[0].text}')
        expected_label1 = 'Password'
        self.assertEqual(label_list[1].text, expected_label1,
                         f'Expected label: {expected_label1}. Actual label: {label_list[1].text}')

    def test_login_secure_and_element_display(self):
        self.chrome.find_element(By.NAME, 'username').send_keys('tomsmith')
        self.chrome.find_element(By.NAME, 'password').send_keys('SuperSecretPassword!')
        self.chrome.find_element(By.CLASS_NAME, 'radius').click()
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/secure'
        assert expected == actual, 'URL is incorrect'
        try:
            wait = WebDriverWait(self.chrome, 10)
            wait.until(expected_conditions.visibility_of_element_located((By.ID, 'flash')))
            wait.until(expected_conditions.text_to_be_present_in_element((By.ID, 'flash'), 'secure area!'))
        except TimeoutException:
            return False
        return True

    def test_z_login_logout(self):
        self.chrome.find_element(By.NAME, 'username').send_keys('tomsmith')
        self.chrome.find_element(By.NAME, 'password').send_keys('SuperSecretPassword!')
        self.chrome.find_element(By.CLASS_NAME, 'radius').click()
        self.chrome.find_element(By.XPATH, "//i[contains(.,'Logout')]").click()

    def test_brute_force_hacking(self):
        passwords_list = self.chrome.find_element(By.XPATH, '//h4').text.split(sep=' ')
        is_found = False
        password_found = None
        for password in range(len(passwords_list)):
            self.chrome.find_element(By.NAME, 'username').send_keys('tomsmith')
            self.chrome.find_element(By.NAME, 'password').send_keys(passwords_list[password])
            self.chrome.find_element(By.CLASS_NAME, 'radius').click()
            actual = self.chrome.current_url
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
