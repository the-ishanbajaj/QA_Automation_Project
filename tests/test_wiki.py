import re
from playwright.sync_api import expect

def test_wikipedia(page):
    page.goto("https://en.wikipedia.org")

    page.locator("#searchInput").fill("Playwright (software)")

    page.locator("button:has-text('Search')").first.click()

    expect(page).to_have_url(re.compile(".*Playwright"))