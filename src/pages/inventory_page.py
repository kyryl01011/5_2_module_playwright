import allure
from src.pages.base_page import BasePage


class InventoryPage(BasePage):
    ADD_TO_CART_BUTTON_SELECTOR = 'div.inventory_item:has-text("Sauce Labs Backpack") >> button#add-to-cart-sauce-labs-backpack'
    REMOVE_FROM_CART_BUTTON_SELECTOR = 'div.inventory_item:has-text("Sauce Labs Backpack") >> button'

    def __init__(self, page: BasePage):
        super().__init__(page)
        self._endpoint = 'inventory.html'

    @allure.title('Adds first item to the cart')
    def add_first_item_to_cart(self):
        self.check_url(self._get_page_url)
        self.clickButton(self.ADD_TO_CART_BUTTON_SELECTOR)
        self.assert_text_present_in_element(self.REMOVE_FROM_CART_BUTTON_SELECTOR, 'Remove')
