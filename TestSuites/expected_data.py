class ExpectedData:
    def __init__(self):
        self.page_title_expected = 'The Internet'
        self.title_expected = 'Login Page'
        self.expected_link = 'http://elementalselenium.com/'
        self.text_expected = 'Your username is invalid!\n×'
        self.username = 'tomsmith'
        self.wrong_username = 'johndoe'
        self.password = 'SuperSecretPassword!'
        self.wrong_password = 'NotASuperPass?'
        self.user_label = 'Username'
        self.password_label = 'Password'
