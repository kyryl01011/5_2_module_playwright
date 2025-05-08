import requests
import pytest
from playwright.sync_api import sync_playwright, expect

from components.header import Header
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

def test_userflow(browser, generate_random_customer_data):
    '''
    Login into account, add first item to cart, checkout and logout
    '''
    firstname = generate_random_customer_data['first-name']
    lastname = generate_random_customer_data['last-name']
    zipcode = generate_random_customer_data['zip-code']
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)
    logout_page = Header(page)
    login_page.login('standard_user', 'secret_sauce')
    inventory_page.add_first_item_to_cart()
    checkout_page.start_checkout()
    checkout_page.fill_checkout_form(firstname, lastname, zipcode)
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



# playwright = sync_playwright().start()
# browser = playwright.chromium.launch(headless=False, slow_mo=50)
# page = browser.new_page()
# page.goto('https://www.w3.org/')
# page.wait_for_load_state('load')
# locator_consortium = page.get_by_text("World Wide Web Consortium", exact=True)
# locator_about = page.get_by_text("About", exact=True)
# locator_standards = page.get_by_text("Standards", exact=True)
# locator_noexist = page.get_by_text("Nonexistent Text", exact=True)
# expect(locator_consortium).to_be_visible, 'Текст не найден' 
# expect(locator_about).to_be_visible, 'Текст не найден'
# expect(locator_standards).to_be_visible, 'Текст не найден' 
# expect(locator_noexist).to_be_hidden, 'Текст найден' 
# browser.close()
# playwright.stop()
