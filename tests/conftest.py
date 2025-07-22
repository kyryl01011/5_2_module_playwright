import allure
import pytest

from playwright.async_api import async_playwright, Browser
from playwright.sync_api import sync_playwright
from faker import Faker

from src.data_models.customer import CustomerCreationModel
from src.pages.login_page import AsyncLoginPage

faker = Faker()


@pytest.fixture(scope='session')
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


@pytest.fixture(scope='class')
async def async_browser():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)

        yield browser

        await browser.close()


@pytest.fixture
async def async_page(async_browser: Browser):
    async_page = await async_browser.new_page()
    yield async_page
    await async_page.close()


@pytest.fixture
async def async_logged_page(async_page):
    login_page = AsyncLoginPage(async_page)
    await login_page.login('standard_user', 'secret_sauce')
    return login_page.page