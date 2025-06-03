from src.pages.base_page import BasePage
import allure


class LoginPage(BasePage):
    INPUT_LOGIN_SELECTOR = 'input#user-name'
    INPUT_PASSWORD_SELECTOR = 'input#password'
    LOGIN_BUTTON_SELECTOR = 'input#login-button'

    def __init__(self, page: BasePage):
        super().__init__(page)
        self._endpoint = ''

    @allure.title('Open website > Fill form > Log in account')
    def login(self, username, password):
        self.navigate_to(self._get_page_url)
        self.wait_page_load(self._get_page_url)
        self.check_url(self._get_page_url)
        self.type_text(self.INPUT_LOGIN_SELECTOR, username)
        self.assert_element_attribute(self.INPUT_LOGIN_SELECTOR, 'value', username)
        self.type_text(self.INPUT_PASSWORD_SELECTOR, password)
        self.assert_element_attribute(self.INPUT_PASSWORD_SELECTOR, 'value', password)
        self.is_element_enabled(self.LOGIN_BUTTON_SELECTOR)
        self.clickButton(self.LOGIN_BUTTON_SELECTOR)
        self.wait_page_load(self._get_page_url)
        self.assert_text_present_on_page('Products')
