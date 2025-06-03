from src.components.header import Header
from src.pages.checkout_page import CheckoutPage
from src.pages.inventory_page import InventoryPage
from src.pages.login_page import LoginPage


def test_user_flow(browser, generated_customer_data):
    """
    Login into account, add first item to cart, checkout and logout
    """
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)
    logout_page = Header(page)
    login_page.login('standard_user', 'secret_sauce')
    inventory_page.add_first_item_to_cart()
    checkout_page.start_checkout()
    checkout_page.fill_checkout_form(generated_customer_data.firstname, generated_customer_data.lastname,
                                     generated_customer_data.zipcode)
    checkout_page.finish_checkout()
    logout_page.log_out()


def test_logout(browser):
    """
    Check login and logout
    """
    page = browser.new_page()
    login_page = LoginPage(page)
    logout_page = Header(page)
    login_page.login('standard_user', 'secret_sauce')
    logout_page.log_out()
