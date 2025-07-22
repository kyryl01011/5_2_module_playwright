from async_pages.base_page import AsyncBasePage
from src.pages.base_page import BasePage
import allure


class LoginPage(BasePage):
    INPUT_LOGIN_SELECTOR = 'input#user-name'
    INPUT_PASSWORD_SELECTOR = 'input#password'
    LOGIN_BUTTON_SELECTOR = 'input#login-button'

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


class AsyncLoginPage(LoginPage, AsyncBasePage):
    @allure.title('Async login user through login page')
    async def login(self, username: str, password: str):
        await self.go_to_page('/')
        await self.assert_page_url_equals('/')
        await self.fill_selector_with_text(self.INPUT_LOGIN_SELECTOR, username)
        await self.assert_element_attr_equals_text(self.INPUT_LOGIN_SELECTOR, 'value', username)
        await self.fill_selector_with_text(self.INPUT_PASSWORD_SELECTOR, password)
        await self.assert_element_attr_equals_text(self.INPUT_PASSWORD_SELECTOR, 'value', password)
        await self.assert_element_enable(self.LOGIN_BUTTON_SELECTOR)
        await self.click_element(self.LOGIN_BUTTON_SELECTOR)
        await self.assert_text_presented_on_page('Products')
