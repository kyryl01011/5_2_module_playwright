import pytest

from src.components.header import AsyncHeader
from src.pages.login_page import AsyncLoginPage

@pytest.mark.async_playwright
@pytest.mark.anyio
class TestAsyncPlaywright:

    @pytest.mark.anyio
    async def test_login(self, async_page):
        # page = await async_browser.new_page()
        login_page = AsyncLoginPage(async_page)
        await login_page.login('standard_user', 'secret_sauce')

    @pytest.mark.anyio
    async def test_logout(self, async_logged_page):
        header_fragment = AsyncHeader(async_logged_page)
        await header_fragment.async_log_out()
