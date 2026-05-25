import re
import pytest
from playwright.sync_api import expect
from pages.SearchPage import Search_Page

@pytest.mark.parametrize("search_term" , [
    "Python ",
    "JavaScript",
    "Playwright (software)",
    "Bajaj"
])
def test_ddt(page , search_term):
    
    search_ui = Search_Page(page)

    search_ui.navigate()
    search_ui.enter_search_term(search_term)
    search_ui.click_btn()

    first_word = search_term.split(" ")[0]

    expect(page.locator("#firstHeading")).to_contain_text(first_word)
    