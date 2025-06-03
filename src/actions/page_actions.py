from playwright.sync_api import Page, expect
import allure


class PageActions:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url):
        with allure.step(f'Go to URL: {url}'):
            self.page.goto(url)

    def check_url(self, url):
        with allure.step(f'Check if current URL is {url}'):
            expect(self.page).to_have_url(url)

    def wait_for_url(self, url):
        with allure.step(f'Wait URL to change to: {url}'):
            self.page.wait_for_url(url)

    def wait_page_load(self, url):
        with allure.step(f'Check if URL {url} loaded'):
            self.page.wait_for_load_state('load')

    def clickButton(self, selector):
        with allure.step(f'Click button with selector {selector}'):
            self.page.click(selector=selector)

    def is_element_present(self, selector):
        with allure.step(f'Check if element is presented on page with selector: {selector}'):
            # self.page.is_visible(selector) ??
            expect(self.page.locator(selector)).to_be_visible()

    def is_element_enabled(self, selector):
        with allure.step(f'Check if element {selector} is enabled'):
            expect(self.page.locator(selector)).to_be_enabled()

    def input_text(self, selector, text):
        with allure.step(f'Fill {selector} with text: "{text}"'):
            self.page.fill(selector, text)

    def type_text(self, selector, text):
        with allure.step(f'Type "{text}" in {selector}'):
            self.page.type(selector, text)

    def wait_element_to_appear(self, selector):
        with allure.step(f'Wait for {selector} to appear'):
            self.page.wait_for_selector(selector, state='visible')

    def wait_element_to_disappear(self, selector):
        with allure.step(f'Wait for {selector} to disappear'):
            self.page.wait_for_selector(selector, state='detached')

    def assert_text_present_on_page(self, text):
        with allure.step(f'Check if text presented in page - {text}'):
            expect(self.page.locator('body')).to_contain_text(text)

    def assert_text_present_in_element(self, selector, text):
        with allure.step(f'Check if text {text} is in element {selector}'):
            expect(self.page.locator(selector)).to_have_text(text)

    def assert_element_attribute(self, selector, attribute, value):
        with allure.step(f'Check if element {selector} has attribute {attribute} with value {value}'):
            expect(self.page.locator(selector)).to_have_attribute(attribute, value)

    def assert_element_is_hidden(self, selector):
        with allure.step(f'Check if element {selector} is hidden'):
            expect(self.page.locator(selector)).to_be_hidden()
