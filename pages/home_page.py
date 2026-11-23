from playwright.sync_api import Page

from pages.login_page import LoginPage


class HomePage:

    def __init__(self, page: Page):
        self.page = page
        self.sign_in_button = page.get_by_role("link", name="Sign in")

    def go_to_login_page(self) -> LoginPage:
        self.sign_in_button.click()
        return LoginPage(self.page)
