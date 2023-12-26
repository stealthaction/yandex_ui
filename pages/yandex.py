from base.base import Base
from playwright.sync_api import Page


class FindPage(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def fill_value_in_search(self, value: str):
        self.page.get_by_placeholder("найдётся всё").fill(value)

    def click_button_find(self):
        self.page.get_by_role("button", name="Найти").click()

    def page_goto(self, url: str):
        self.page.goto(url)