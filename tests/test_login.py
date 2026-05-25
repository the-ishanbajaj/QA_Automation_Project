import pytest
import re

from playwright.sync_api import expect
from pages.login_page import LoginPage


def test_login(page) :

    login_ui = LoginPage(page)
    login_ui.navigate()

    login_ui.login("standard_user","secret_sauce")

    expect(page).to_have_url(re.compile(".*inventory.html"))

@pytest.mark.parametrize("username, password, expected_error", [
    ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out."),
    ("standard_user", "wrong_password", "Username and password do not match"),
    ("", "secret_sauce", "Username is required"),
])

def test_invalid_logins(page , username , password , expected_error):

    login_ui = LoginPage(page)
    login_ui.navigate()

    login_ui.login(username,password)

    error_text = login_ui.get_error()
    expect(login_ui.error_message).to_contain_text(expected_error)