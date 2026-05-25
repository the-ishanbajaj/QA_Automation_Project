class Search_Page:
    def __init__(self,page):
        self.page = page

    
        self.search_box = page.locator("#searchInput")
        self.sub_btn = page.get_by_role("button" , name ="Search").first

    def navigate(self):
        self.page.goto("https://en.wikipedia.org")

    def enter_search_term(self,text):
        self.search_box.fill(text)

    def click_btn(self):
        self.sub_btn.click()
