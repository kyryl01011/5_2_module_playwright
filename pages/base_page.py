import allure
from playwright.sync_api import Page, expect
from actions.page_actions import PageActions

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.__base_url = 'https://www.saucedemo.com/'
        self._endpoint = ''
        self.action = PageActions(page)

    @property
    def _get_page_url(self):
        return self.__base_url + self._endpoint
    
    @_get_page_url.setter
    def _get_page_url(self, endpoint):
        self._endpoint = endpoint


