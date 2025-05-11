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
