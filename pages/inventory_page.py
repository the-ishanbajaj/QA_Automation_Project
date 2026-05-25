class InventoryPage :
    def __init__(self ,page):
        self.page = page

        self.backpack_add_button = page.locator("[data-test = 'add-to-cart-sauce-labs-backpack']")
        self.cart_badge = page.locator(".shopping_cart_badge")


    def add_to_cart(self):
        self.backpack_add_button.click()

    def get_cart_badge(self):
        return self.cart_badge.inner_text()
    