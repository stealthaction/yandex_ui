from pages.yandex import FindPage
import pytest


class TestSearch:
    @pytest.mark.ui
    def test_search(self, find_page: FindPage):
        find_page.page_goto('ya.ru')
        find_page.fill_value_in_search('Человек паук')
        find_page.click_button_find()
