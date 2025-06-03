from playwright.sync_api import Page, expect
import allure


class PageActions:
    def __init__(self, page: Page):
        self.page = page


