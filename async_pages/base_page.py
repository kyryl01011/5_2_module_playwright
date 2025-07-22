import allure
from playwright.async_api import Page, expect

from src.enums.base_urls import URL


class AsyncBasePage:
    def __init__(self, page: Page):
        self.page = page

    @staticmethod
    def build_url(endpoint: str) -> str:
        return URL.BASE_DOMAIN.value + endpoint

    async def go_to_page(self, endpoint: str):
        with allure.step(f'Go to page with URL : {self.build_url(endpoint)}'):
            await self.page.goto(self.build_url(endpoint))
            await self.page.wait_for_load_state('load')

    async def click_element(self, selector: str):
        with allure.step(f'Click element with selector: {selector}'):
            await self.page.click(selector)

    async def wait_for_selector(self, selector: str):
        with allure.step(f'Wait for selector: {selector}'):
            await self.page.wait_for_selector(selector)

    async def fill_selector_with_text(self, selector, text):
        with allure.step(f'Fill selector {selector} with text: {text}'):
            await self.page.fill(selector, text)

    async def assert_page_url_equals(self, expected_url: str):
        with allure.step(f'Assert current page URL equals to {self.build_url(expected_url)}'):
            expected_url = self.build_url(expected_url)
            cur_url = self.page.url
            assert cur_url == expected_url, f'Current URL not equals to expected: {expected_url}'
            await expect(self.page).to_have_url(expected_url)

    async def assert_element_attr_equals_text(self, selector: str, attr: str, exp_text: str):
        with allure.step(f'Assert that expected {selector} with attribute {attr} has text that equals {exp_text}'):
            await expect(self.page.locator(selector)).to_have_attribute(attr, exp_text)

    async def assert_element_enable(self, selector: str):
        with allure.step(f'Assert that {selector} element is enabled'):
            await expect(self.page.locator(selector)).to_be_enabled()

    async def assert_text_presented_on_page(self, text: str):
        with allure.step(f'Assert text "{text}" is presented on page {self.page.url}'):
            await expect(self.page.locator('body')).to_contain_text(text)
