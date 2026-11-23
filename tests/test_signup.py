import pytest
from playwright.sync_api import expect

from models.user import User
from pages.account_page import AccountPage
from pages.login_page import LoginPage


def test_signup_success_and_login_after(home_page):
    user = User()
    login_page = home_page.go_to_login_page()
    signup_page = login_page.go_to_signup_page()
    signup_page.fill_in_registration_form(user)
    signup_page.click_register_button()
    login_page = LoginPage(signup_page.page)

    expect(login_page.login_title).to_be_visible()
    expect(login_page.page).to_have_url(login_page.URL)

    login_page.fill_in_login_form(user.email, user.password)
    login_page.click_login_button()
    account_page = AccountPage(login_page.page)

    expect(account_page.title_my_account).to_be_visible()


INVALID_SIGNUP_CASES = [
    pytest.param(User(first_name=""), "First name is required", "first-name", id="empty_first_name"),
    pytest.param(User(password="12345567"), "Password can not include invalid characters.", "password", id="wrong_password_format"),
    pytest.param(User(dob="44444444"), "Please enter a valid date in YYYY-MM-DD format.", "dob", id="invalid_dob_format"),
    pytest.param(User(email="johndoe.com"), "Email format is invalid", "email", id="invalid_email_format")
]


@pytest.mark.parametrize("user, expected_error, field_name", INVALID_SIGNUP_CASES)
def test_signup_fails_with_invalid_data(home_page, user, expected_error, field_name):
    login_page = home_page.go_to_login_page()
    signup_page = login_page.go_to_signup_page()
    signup_page.fill_in_registration_form(user)
    signup_page.click_register_button()

    expect(signup_page.alert_locator(field_name)).to_contain_text(expected_error)
    expect(signup_page.page).to_have_url(signup_page.URL)





