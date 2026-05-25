import re
from pages.SearchPage import Search_Page
from playwright.sync_api import expect

def test_wikipedia_search(page):
    

    search_ui = Search_Page(page)

    search_ui.navigate()
    search_ui.enter_search_term("Python (programming language)")

    search_ui.click_btn()

    
    expect(page).to_have_url(re.compile(".*Python"))