from src.pages.base_page import BasePage
import allure


class CheckoutPage(BasePage):
    CHECKOUT_BUTTON_SELECTOR = 'button#checkout'
    FIRSTNAME_INPUT_SELECTOR = 'input[placeholder="First Name"]'
    LASTNAME_INPUT_SELECTOR = 'input[placeholder="Last Name"]'
    ZIP_INPUT_SELECTOR = 'input[placeholder="Zip/Postal Code"]'
    CONTINUE_BUTTON_SELECTOR = 'input[value="Continue"]'
    FINISH_BUTTON_SELECTOR = 'button#finish'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'cart.html'

    @allure.title('Open checkout page > go to checkout form')
    def start_checkout(self):
        self.navigate_to(self._get_page_url)
        self.wait_page_load(self._get_page_url)
        self.check_url(self._get_page_url)
        self.is_element_enabled(self.CHECKOUT_BUTTON_SELECTOR)
        self.clickButton(self.CHECKOUT_BUTTON_SELECTOR)
        self.wait_element_to_appear(self.FIRSTNAME_INPUT_SELECTOR)

    @allure.title('Fill checkout form')
    def fill_checkout_form(self, firstname, lastname, zipcode):
        self.type_text(self.FIRSTNAME_INPUT_SELECTOR, firstname)
        self.type_text(self.LASTNAME_INPUT_SELECTOR, lastname)
        self.type_text(self.ZIP_INPUT_SELECTOR, zipcode)

    @allure.title('Finish checkout')
    def finish_checkout(self):
        self.clickButton(self.CONTINUE_BUTTON_SELECTOR)
        self.wait_element_to_appear(self.FINISH_BUTTON_SELECTOR)
        self.is_element_enabled(self.FINISH_BUTTON_SELECTOR)
        self.clickButton(self.FINISH_BUTTON_SELECTOR)
        self.assert_text_present_on_page('Thank you for your order!')
