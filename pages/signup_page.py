from playwright.sync_api import Page, Locator

from models.user import User


class SignupPage:
    URL = "https://practicesoftwaretesting.com/auth/register"

    def __init__(self, page: Page):
        self.page = page
        self.customer_registration_title = page.get_by_role("heading", name="Customer registration")
        self.first_name_field = page.get_by_label("First name")
        self.last_name_field = page.get_by_label("Last name")
        self.dob_field = page.get_by_label("Date of Birth")
        self.country_field = page.get_by_label("Country")
        self.postal_code_field = page.get_by_label("Postal code")
        self.house_number_field = page.get_by_label("House number")
        self.street_field = page.get_by_label("Street")
        self.city_field = page.get_by_label("City")
        self.state_field = page.get_by_label("State")
        self.phone_field = page.get_by_label("Phone")
        self.email_field = page.get_by_label("Email address")
        self.password_field = page.get_by_label("Password")
        self.register_button = page.get_by_role("button", name="Register")

    def fill_in_registration_form(self, user: User):
        self.first_name_field.fill(user.first_name)
        self.last_name_field.fill(user.last_name)
        self.dob_field.fill(user.dob)
        self.country_field.select_option(user.country)
        self.postal_code_field.fill(user.postal_code)
        self.house_number_field.fill(user.house_number)
        self.street_field.fill(user.street)
        self.city_field.fill(user.city)
        self.state_field.fill(user.state)
        self.phone_field.fill(user.phone)
        self.email_field.fill(user.email)
        self.password_field.fill(user.password)


    def click_register_button(self):
        self.register_button.click()

    def alert_locator(self, field_name: str) -> Locator:
        return self.page.locator(f'[data-test="{field_name}-error"]')
