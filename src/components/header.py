from async_pages.base_page import AsyncBasePage
from src.pages.base_page import BasePage


class Header(BasePage):
    BURGER_MENU_SELECTOR = 'div.bm-burger-button'
    LOGOUT_BUTTON_SELECTOR = 'a#logout_sidebar_link:has-text("Logout")'

    def log_out(self):
        self.clickButton(self.BURGER_MENU_SELECTOR)
        self.wait_element_to_appear(self.LOGOUT_BUTTON_SELECTOR)
        self.clickButton(self.LOGOUT_BUTTON_SELECTOR)
        self.assert_text_present_on_page('secret_sauce')
        


class AsyncHeader(AsyncBasePage, Header):
    async def async_log_out(self):
        await self.click_element(self.BURGER_MENU_SELECTOR)
        await self.wait_for_selector(self.LOGOUT_BUTTON_SELECTOR)
        await self.click_element(self.LOGOUT_BUTTON_SELECTOR)
        await self.assert_text_presented_on_page('secret_sauce')