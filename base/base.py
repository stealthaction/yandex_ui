from playwright.sync_api import Page


class Base:
    def __init__(self, page: Page):
        self.page = page

    def fill(self, selector: str, value: str) -> None:
        self.page.fill(selector, value)

    def click(self, selector: str) -> None:
        self.page.click(selector)

    def click_first_element(self, selector: str) -> None:
        self.page.locator(selector).nth(0).click()

    def update_page(self) -> None:
        self.page.reload()

    def clear(self, selector: str) -> None:
        self.page.locator(selector).clear()

