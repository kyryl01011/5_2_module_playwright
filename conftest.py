import allure
import pytest
from playwright.sync_api import sync_playwright
from faker import Faker

from src.data_models.customer import CustomerCreationModel


faker = Faker()


@pytest.fixture
def anyio_backend():
    return 'asyncio'


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
def generated_customer_data() -> CustomerCreationModel:
    return CustomerCreationModel(
        firstname=faker.first_name(),
        lastname=faker.last_name(),
        zipcode=faker.zipcode()
    )

@pytest.fixture.anyio
