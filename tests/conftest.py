import pytest

from pages.yandex import FindPage
from playwright.sync_api import Page


@pytest.fixture
def find_page(page: Page) -> FindPage:
    """That's function"""
    return FindPage(page)
