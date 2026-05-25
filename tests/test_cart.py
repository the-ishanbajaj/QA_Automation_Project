
from pages.login_page import LoginPage

def test_addToCart(page):
    login_ui = LoginPage(page)
    login_ui.navigate()

    inventory_ui = login_ui.login("standard_user", "secret_sauce")
    
    inventory_ui.add_to_cart()
    badge_value = inventory_ui.get_cart_badge()

    assert badge_value == "1" , "error"
