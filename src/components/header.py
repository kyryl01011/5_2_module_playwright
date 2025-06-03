from src.pages.base_page import BasePage

class Header(BasePage):
    BURGER_MENU_SELECTOR = 'div.bm-burger-button'
    LOGOUT_BUTTON_SELECTOR = 'a#logout_sidebar_link:has-text("Logout")'

    def __init__(self, page):
        super().__init__(page)

    def log_out(self):
        self.action.clickButton(self.BURGER_MENU_SELECTOR)
        self.action.wait_element_to_appear(self.LOGOUT_BUTTON_SELECTOR)
        self.action.clickButton(self.LOGOUT_BUTTON_SELECTOR)
        self.action.assert_text_present_on_page('secret_sauce')