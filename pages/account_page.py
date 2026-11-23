from playwright.sync_api import Page


class AccountPage:

    def __init__(self, page: Page):
        self.page = page
        self.title_my_account = page.get_by_role("heading", name="My account")
