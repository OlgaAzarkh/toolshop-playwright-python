from playwright.sync_api import Page

from pages.signup_page import SignupPage


class LoginPage:

    URL = "https://practicesoftwaretesting.com/auth/login"

    def __init__(self, page: Page):
        self.page = page
        self.login_title = page.get_by_role("heading", name="Login")
        self.email_input = page.get_by_label("Email address *")
        self.password_input = page.get_by_label("Password *")
        self.login_button = page.get_by_role("button", name="Login")
        self.invalid_email_or_password_error = page.get_by_text("Invalid email or password")
        self.signup_button = page.get_by_role("link", name="Register your account")

    def fill_in_login_form(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)

    def click_login_button(self):
        self.login_button.click()

    def go_to_signup_page(self) -> SignupPage:
        self.signup_button.click()
        return SignupPage(self.page)
