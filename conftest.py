import allure
import pytest
import requests
from playwright.sync_api import sync_playwright
from faker import Faker

# @pytest.fixture(scope='session')
# def auth_session():
#     session = requests.Session()
#     session.headers.update(HEADERS)
#     response = session.post(f'{BASE_URL}/api/v1/login/test-token')
#     print(response.json())

faker = Faker()

@pytest.fixture(scope='session')
@allure.title('Initialize playwright and browser > Close after use')
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    yield browser
    browser.close()
    playwright.stop()

@pytest.fixture(scope='module')
@allure.title('Generate random user data for checkout')
def generate_random_customer_data():
    return {'first-name': faker.first_name(), 'last-name': faker.last_name(), 'zip-code': faker.zipcode()}